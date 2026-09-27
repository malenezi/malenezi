-- Analyst-facing query over the conformed star.
--
-- Note what it does NOT do: it does not recompute an aggregate from silver.
-- The star IS the interface. The moment a dashboard reaches past it into
-- silver, that dashboard has its own definition of "revenue" and the numbers
-- stop reconciling — which is the whole "reporting divergence" case study.
--
--   python -m masar.tools.sql --file serving/queries/exec_demand_dashboard.sql
SELECT
    z.city,
    z.zone_name_en,
    d.full_date,
    COUNT(*)                                    AS trips,
    ROUND(SUM(f.fare_sar), 2)                   AS revenue_sar,
    ROUND(AVG(f.duration_min), 1)               AS avg_duration_min,
    ROUND(AVG(f.surge_multiplier), 3)           AS avg_surge,
    COUNT(DISTINCT f.driver_key)                AS active_drivers
FROM gold.fact_trip f
JOIN gold.dim_date d ON f.date_key        = d.date_key
JOIN gold.dim_zone z ON f.pickup_zone_key = z.zone_key
WHERE d.full_date >= current_date() - INTERVAL 7 DAYS
GROUP BY z.city, z.zone_name_en, d.full_date
ORDER BY d.full_date DESC, revenue_sar DESC
LIMIT 20;
