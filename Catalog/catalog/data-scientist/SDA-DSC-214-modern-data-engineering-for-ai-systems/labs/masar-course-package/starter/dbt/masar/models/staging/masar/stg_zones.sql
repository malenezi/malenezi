-- Staging: 1:1 with bronze.zones. Bilingual labels are kept as delivered —
-- the Arabic zone name is a label, not a translation to be regenerated.
{{ config(materialized='view') }}

with source as (
    select * from {{ source('bronze', 'zones') }}
),

deduped as (
    select * from (
        select *, row_number() over (
            partition by zone_id order by _ingested_at desc, _batch_id desc
        ) as _rn
        from source
    )
    where _rn = 1
)

select
    cast(zone_id      as string)  as zone_id,
    cast(zone_name_en as string)  as zone_name_en,
    cast(zone_name_ar as string)  as zone_name_ar,
    case upper(trim(city))
        when 'RUH' then 'Riyadh'
        when 'JED' then 'Jeddah'
        when 'DMM' then 'Dammam'
        else initcap(trim(city))
    end                           as city,
    cast(district     as string)  as district,
    -- Zone CENTROID, not per-trip coordinates. A district-level point is
    -- public geography; a metre-resolution trace is sensitive location.
    cast(centroid_lat as double)  as centroid_lat,
    cast(centroid_lon as double)  as centroid_lon,
    _batch_id,
    _ingested_at
from deduped
where zone_id is not null
