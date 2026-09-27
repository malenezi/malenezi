{{ config(
    materialized='incremental',
    file_format='delta',
    alias='zone_hourly_demand',
    unique_key=['city', 'pickup_zone_id', 'demand_date', 'demand_hour'],
    incremental_strategy='merge',
    partition_by=['demand_date']
) }}
-- gold.zone_hourly_demand — GRAIN: one row per (city, pickup_zone_id, date, hour).
--
-- The BI demand mart, and one of the two inputs the surge model reads. Because
-- surge acts on it, a double-counted row here is not a reporting error: it is
-- a price. `incremental_strategy='merge'` on the full grain key makes a rerun
-- a no-op, which is the property that keeps that from happening.
--
-- Built from silver.trips, never from bronze: the quality gate sits upstream
-- of silver, and a mart sourced from bronze bypasses every control you built.
with trips as (

    select * from {{ ref('silver_trips') }}
    where status = 'completed'

    {% if is_incremental() %}
      and to_date(pickup_ts) >= current_date() - interval {{ var('lookback_days', 3) }} days
    {% endif %}

)

select
    city,
    pickup_zone_id,
    to_date(pickup_ts)                          as demand_date,
    hour(pickup_ts)                             as demand_hour,
    count(*)                                    as trips,
    count(distinct driver_id)                   as active_drivers,
    round(avg(fare_sar), 2)                     as avg_fare_sar,
    round(sum(fare_sar), 2)                     as revenue_sar,
    round(avg(duration_min), 2)                 as avg_duration_min,
    round(avg(distance_km), 3)                  as avg_distance_km,
    round(avg(surge_multiplier), 3)             as avg_surge,
    current_timestamp()                         as _built_at
from trips
group by city, pickup_zone_id, to_date(pickup_ts), hour(pickup_ts)
