{{ config(materialized='table', file_format='delta', alias='dim_driver') }}
-- gold.dim_driver — GRAIN: one row per driver_id (type-1, current attributes).
--
-- PDPL: national_id_hash and phone_hash are NOT selected. The classification
-- in docs/GOVERNANCE_TEMPLATE.md drives this select list, not convenience —
-- "we might need it later" is how pseudonymised identifiers reach a dashboard.
select
    d.driver_id                                          as driver_key,
    d.driver_id,
    d.full_name_en,
    d.city,
    d.hire_date,
    d.rating,
    d.status,
    datediff(current_date(), d.hire_date)                as tenure_days,
    case when datediff(current_date(), d.hire_date) < 90  then 'new'
         when datediff(current_date(), d.hire_date) < 365 then 'established'
         else 'veteran' end                              as tenure_band
from {{ ref('silver_drivers') }} d
