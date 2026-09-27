-- silver.drivers — conformed driver roster. GRAIN: one row per driver_id.
-- Type-1: current attributes only. Masar does not need driver history to run
-- the network, and keeping it would extend a personal-data retention window
-- for no stated purpose.
{{ config(
    materialized='table',
    file_format='delta',
    schema='silver',
    alias='drivers'
) }}

select
    driver_id,
    full_name_en,                 -- PDPL: personal data; dim_driver may expose, BI may not
    city,
    hire_date,
    rating,
    status,
    national_id_hash,             -- PDPL: pseudonymised; never crosses the serving boundary
    phone_hash,                   -- PDPL: pseudonymised
    datediff(current_date(), hire_date) as tenure_days,
    _ingested_at,
    current_timestamp()           as _loaded_at
from {{ ref('stg_drivers') }}
where driver_id is not null
