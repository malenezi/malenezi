-- Staging: flatten bronze.gps_events' nested payload and normalise the speed
-- unit. One row per ping as landed; deduplication happens in silver, where a
-- watermark bounds the state it costs.
{{ config(materialized='view') }}

with source as (

    select * from {{ source('bronze', 'gps_events') }}

),

flattened as (

    select
        cast(event_id   as string)         as event_id,
        cast(vehicle_id as string)         as vehicle_id,
        cast(driver_id  as string)         as driver_id,     -- PDPL: personal data
        cast(trip_id    as string)         as trip_id,
        cast(ts         as timestamp)      as event_ts,      -- EVENT time, from the device
        cast(payload.lat         as double) as lat,          -- PDPL: sensitive location
        cast(payload.lon         as double) as lon,          -- PDPL: sensitive location
        cast(payload.heading_deg as double) as heading_deg,
        cast(payload.accuracy_m  as double) as accuracy_m,
        cast(producer_version as string)   as producer_version,

        -- THE SIGNATURE INCIDENT. Producer 2.5.0 emits the SAME KEY
        -- `speed_kmh` with the SAME TYPE and metres-per-second VALUES.
        -- Type-compatible, so schema validation passes; in range, so range
        -- checks pass. Only a per-version distribution comparison sees it.
        -- The conversion belongs here, at the conforming boundary, so every
        -- downstream consumer gets km/h without knowing this ever happened.
        case
            when producer_version = '2.5.0' then cast(payload.speed_kmh as double) * 3.6
            else cast(payload.speed_kmh as double)
        end                                as speed_kmh,

        _batch_id,
        _ingested_at

    from source
    where event_id is not null

)

select * from flattened
