{{ config(materialized='table', file_format='delta', alias='dim_vehicle') }}
-- gold.dim_vehicle — GRAIN: one row per vehicle_id.
select
    v.vehicle_id                                         as vehicle_key,
    v.vehicle_id,
    v.plate_hash,                       -- pseudonymised at source; kept for ops lookup
    v.make,
    v.model,
    v.model_year,
    v.capacity,
    v.fuel_type,
    v.city,
    year(current_date()) - v.model_year                  as vehicle_age_years,
    case when v.capacity >= 11 then 'van'
         when v.capacity >= 7  then 'suv'
         else 'saloon' end                               as vehicle_class
from {{ ref('stg_vehicles') }} v
