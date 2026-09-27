-- Staging: 1:1 with bronze.trips. Rename, cast, normalise. NO joins, NO
-- business logic, NO filtering beyond dropping rows that cannot be keyed.
--
-- Everything that is "the source is weird" belongs here and only here, so
-- exactly one file has to change when the source gets weirder.
{{ config(materialized='view') }}

with source as (

    select * from {{ source('bronze', 'trips') }}

),

parsed as (

    select
        cast(trip_id          as string)  as trip_id,
        cast(rider_id         as string)  as rider_id,     -- PDPL: personal data
        cast(driver_id        as string)  as driver_id,
        cast(vehicle_id       as string)  as vehicle_id,

        -- The raw feed carries city CODES (RUH/JED/DMM); every conformed layer
        -- carries city NAMES. Map once, here, or nine downstream models each
        -- invent their own mapping and the dashboards stop reconciling.
        case upper(trim(city))
            when 'RUH' then 'Riyadh'
            when 'JED' then 'Jeddah'
            when 'DMM' then 'Dammam'
            when 'MKK' then 'Mecca'
            when 'MED' then 'Medina'
            else initcap(trim(city))      -- unknown codes survive to be quarantined
        end                               as city,

        cast(pickup_zone_id   as string)  as pickup_zone_id,
        cast(dropoff_zone_id  as string)  as dropoff_zone_id,

        -- The source ships TWO timestamp formats (~2% use dd/MM/yyyy HH:mm).
        -- Parse both, coalesce, then normalise Asia/Riyadh wall clock -> UTC
        -- ONCE. Store UTC, present +03: mixing the two is how a "midnight"
        -- report ends up covering 21:00 to 21:00.
        to_utc_timestamp(
            coalesce(
                to_timestamp(pickup_ts,  'yyyy-MM-dd HH:mm:ss'),
                to_timestamp(pickup_ts,  'dd/MM/yyyy HH:mm')
            ), 'Asia/Riyadh')             as pickup_ts,
        to_utc_timestamp(
            coalesce(
                to_timestamp(dropoff_ts, 'yyyy-MM-dd HH:mm:ss'),
                to_timestamp(dropoff_ts, 'dd/MM/yyyy HH:mm')
            ), 'Asia/Riyadh')             as dropoff_ts,

        cast(distance_km      as double)  as distance_km,
        cast(duration_min     as double)  as reported_duration_min,  -- as delivered; may be negative
        cast(fare_sar         as double)  as fare_sar,
        cast(surge_multiplier as double)  as surge_multiplier,
        lower(trim(payment_type))         as payment_type,
        lower(trim(status))               as status,

        -- '' is MISSING, not a value. 3.1% of rows are empty here by design;
        -- leaving them as '' makes every downstream null check report clean.
        nullif(trim(dropoff_geohash), '') as dropoff_geohash,

        -- lineage carried forward from bronze (Lab 1)
        _batch_id,
        _ingested_at,
        _source_file

    from source
    where trip_id is not null             -- drop unkeyed garbage at the boundary

)

select * from parsed
