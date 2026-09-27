{{ config(
    materialized='incremental',
    file_format='delta',
    alias='fact_trip',
    unique_key='trip_id',
    incremental_strategy='merge',
    partition_by=['pickup_date']
) }}
-- gold.fact_trip — GRAIN: exactly one row per trip_id.
--
-- Foreign keys to CONFORMED dimensions, measures at trip grain, nothing else.
-- PDPL: rider_id is NOT selected. It never crosses the serving boundary. A
-- pseudonym is provided so cohort questions ("do repeat riders take longer
-- trips?") remain answerable without exposing the identifier.
select
    t.trip_id,
    cast(date_format(t.pickup_ts, 'yyyyMMdd') as int)    as date_key,
    t.driver_id                                          as driver_key,
    t.vehicle_id                                         as vehicle_key,
    t.pickup_zone_id                                     as pickup_zone_key,
    t.dropoff_zone_id                                    as dropoff_zone_key,
    sha2(t.rider_id, 256)                                as rider_pseudonym,
    to_date(t.pickup_ts)                                 as pickup_date,
    t.pickup_ts,
    t.dropoff_ts,
    t.city,
    t.payment_type,
    t.status,
    -- measures
    t.fare_sar,
    t.distance_km,
    t.duration_min,
    t.surge_multiplier,
    round(t.fare_sar / nullif(t.distance_km, 0), 3)      as fare_per_km_sar
from {{ ref('silver_trips') }} t
where t.status = 'completed'
{% if is_incremental() %}
  and to_date(t.pickup_ts) >= current_date() - interval {{ var('lookback_days', 3) }} days
{% endif %}
