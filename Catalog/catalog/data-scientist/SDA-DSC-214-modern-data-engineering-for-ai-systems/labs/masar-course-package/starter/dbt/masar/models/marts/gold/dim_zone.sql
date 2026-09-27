{{ config(materialized='table', file_format='delta', alias='dim_zone') }}
-- gold.dim_zone — GRAIN: one row per zone_id.
--
-- Bilingual labels; centroid at ZONE resolution. That is the PDPL
-- minimisation line: a district centroid answers "where is demand?"; a
-- per-trip coordinate answers "where does this person live?", which is a
-- question the BI layer was never asked.
select
    z.zone_id                                            as zone_key,
    z.zone_id,
    z.zone_name_en,
    z.zone_name_ar,
    z.city,
    z.district,
    z.centroid_lat,
    z.centroid_lon
from {{ ref('stg_zones') }} z
