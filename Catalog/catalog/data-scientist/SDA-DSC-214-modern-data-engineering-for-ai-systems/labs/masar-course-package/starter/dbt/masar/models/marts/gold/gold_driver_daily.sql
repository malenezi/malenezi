{{ config(
    materialized='incremental',
    file_format='delta',
    alias='driver_daily',
    unique_key=['driver_id', 'activity_date'],
    incremental_strategy='merge',
    partition_by=['activity_date']
) }}
-- gold.driver_daily — GRAIN: one row per (driver_id, date).
--
-- Deliberately NOT partitioned by (city, date, driver_id): that would produce
-- ~14,000 directories per day, turn an 800 ms dashboard query into 40 s, and
-- triple the object-storage request bill. Partition by date; ZORDER the rest.
with trips as (

    select * from {{ ref('silver_trips') }}

    {% if is_incremental() %}
      where to_date(pickup_ts) >= current_date() - interval {{ var('lookback_days', 3) }} days
    {% endif %}

),

daily as (

    select
        driver_id,
        to_date(pickup_ts)                      as activity_date,
        count(*)                                as trips,
        sum(case when status = 'completed' then 1 else 0 end)      as trips_completed,
        sum(case when status like 'cancelled%' then 1 else 0 end)  as trips_cancelled,
        round(sum(fare_sar), 2)                 as gross_earnings_sar,
        round(sum(distance_km), 2)              as distance_km,
        round(sum(duration_min), 1)             as on_trip_minutes,
        round(avg(surge_multiplier), 3)         as avg_surge
    from trips
    group by driver_id, to_date(pickup_ts)

)

select
    d.driver_id,
    d.activity_date,
    d.trips,
    d.trips_completed,
    d.trips_cancelled,
    d.gross_earnings_sar,
    d.distance_km,
    d.on_trip_minutes,
    d.avg_surge,
    round(d.trips_completed / nullif(d.trips, 0), 4)   as completion_rate,
    dr.city,
    dr.rating,
    dr.status,
    current_timestamp()                                as _built_at
from daily d
left join {{ ref('silver_drivers') }} dr on d.driver_id = dr.driver_id
