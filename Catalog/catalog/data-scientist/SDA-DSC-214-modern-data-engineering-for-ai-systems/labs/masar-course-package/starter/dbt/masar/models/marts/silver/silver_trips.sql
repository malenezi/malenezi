-- silver.trips — THE conformed contract. One row per completed, valid trip.
--
-- Three properties, each earned by one specific decision below:
--   * incremental + merge on trip_id  => idempotent. Re-running is safe.
--   * lookback window on pickup_ts    => late-arriving trips are CORRECTED,
--                                        not missed.
--   * dedupe to latest _ingested_at   => the correction batch wins, always.
{{ config(
    materialized='incremental',
    incremental_strategy='merge',
    unique_key='trip_id',
    file_format='delta',
    schema='silver',
    alias='trips',
    partition_by=['city'],
    on_schema_change='append_new_columns'
) }}

with trips as (

    select * from {{ ref('stg_trips') }}

    {% if is_incremental() %}
      -- LOOKBACK: reprocess a {{ var('lookback_days', 3) }}-day window so
      -- late-arriving trips are merged rather than lost.
      --
      -- The window is on pickup_ts (EVENT time), not on _ingested_at
      -- (processing time). A trip that ENDED yesterday but ARRIVED today must
      -- fall inside it; filtering on _ingested_at would let it in but would
      -- also silently drop a corrected row that arrived with an older stamp.
      where pickup_ts >= (
          select date_sub(max(pickup_ts), {{ var('lookback_days', 3) }})
          from {{ this }}
      )
    {% endif %}

),

deduped as (

    -- Bronze is append-only, so the same trip_id can appear in several
    -- batches. Keep the LATEST landed version per key. `distinct` would keep
    -- an arbitrary row, which on a correction batch means keeping the stale
    -- fare roughly half the time — silently, and only for corrected trips.
    select * from (
        select
            *,
            row_number() over (
                partition by trip_id
                order by _ingested_at desc, _batch_id desc
            ) as _rn
        from trips
    )
    where _rn = 1

),

drivers as (

    select driver_id, rating as driver_rating, status as driver_status
    from {{ ref('stg_drivers') }}

),

joined as (

    select
        d.trip_id,
        d.rider_id,                                    -- PDPL: never leaves silver un-masked
        d.driver_id,
        d.vehicle_id,
        d.city,
        d.pickup_zone_id,
        d.dropoff_zone_id,
        d.pickup_ts,                                   -- UTC
        d.dropoff_ts,                                  -- UTC
        to_date(from_utc_timestamp(d.pickup_ts, 'Asia/Riyadh')) as trip_date,  -- business date, +03
        d.distance_km,
        d.reported_duration_min,                       -- as delivered; may disagree with the truth
        round((unix_timestamp(d.dropoff_ts)
               - unix_timestamp(d.pickup_ts)) / 60.0, 2)        as duration_min,  -- derived truth
        d.fare_sar,
        d.surge_multiplier,
        d.payment_type,
        d.status,
        d.dropoff_geohash,
        dr.driver_rating,
        dr.driver_status,
        round(d.fare_sar / nullif(d.distance_km, 0), 3)         as fare_per_km,
        hour(from_utc_timestamp(d.pickup_ts, 'Asia/Riyadh'))    as pickup_hour,
        dayofweek(from_utc_timestamp(d.pickup_ts, 'Asia/Riyadh')) as day_of_week,
        case when hour(from_utc_timestamp(d.pickup_ts, 'Asia/Riyadh')) < 6
             then 1 else 0 end                                   as is_night,
        d._batch_id,
        d._ingested_at,
        current_timestamp()                                      as _loaded_at

    from deduped d
    left join drivers dr on d.driver_id = dr.driver_id

    -- silver = conformed, valid, COMPLETED trips. Everything filtered out here
    -- still exists in bronze; nothing is destroyed, only excluded from the
    -- contract downstream consumers are allowed to rely on.
    where d.status = 'completed'
      and d.dropoff_ts > d.pickup_ts     -- reject impossible durations
      and d.fare_sar > 0                 -- reject non-positive fares
      and d.distance_km > 0

)

select * from joined
