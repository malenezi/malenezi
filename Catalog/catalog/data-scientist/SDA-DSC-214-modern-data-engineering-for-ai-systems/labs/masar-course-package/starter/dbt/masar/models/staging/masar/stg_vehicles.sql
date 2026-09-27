-- Staging: 1:1 with bronze.vehicles. Reference data; conform the city code.
{{ config(materialized='view') }}

with source as (
    select * from {{ source('bronze', 'vehicles') }}
),

deduped as (
    select * from (
        select *, row_number() over (
            partition by vehicle_id order by _ingested_at desc, _batch_id desc
        ) as _rn
        from source
    )
    where _rn = 1
)

select
    cast(vehicle_id as string)  as vehicle_id,
    cast(plate_hash as string)  as plate_hash,     -- PDPL: pseudonymised at source
    cast(make       as string)  as make,
    cast(model      as string)  as model,
    cast(model_year as int)     as model_year,
    cast(capacity   as int)     as capacity,
    lower(trim(fuel_type))      as fuel_type,
    case upper(trim(city))
        when 'RUH' then 'Riyadh'
        when 'JED' then 'Jeddah'
        when 'DMM' then 'Dammam'
        else initcap(trim(city))
    end                         as city,
    _batch_id,
    _ingested_at
from deduped
where vehicle_id is not null
