-- Reconciliation: the star and the demand mart must agree, to the halala.
--
-- Two products, one source of truth. If this returns rows, one of the two is
-- wrong and no dashboard built on either can be trusted until you know which.
-- Run it after every gold build; it costs seconds and it is the cheapest
-- evidence you will ever produce for a steering committee.
WITH from_star AS (
    SELECT d.full_date AS d, ROUND(SUM(f.fare_sar), 2) AS revenue_sar
    FROM gold.fact_trip f
    JOIN gold.dim_date d ON f.date_key = d.date_key
    GROUP BY d.full_date
),
from_mart AS (
    SELECT demand_date AS d, ROUND(SUM(revenue_sar), 2) AS revenue_sar
    FROM gold.zone_hourly_demand
    GROUP BY demand_date
)
SELECT
    s.d,
    s.revenue_sar        AS star_revenue_sar,
    m.revenue_sar        AS mart_revenue_sar,
    ROUND(s.revenue_sar - m.revenue_sar, 2) AS difference_sar
FROM from_star s
JOIN from_mart m ON s.d = m.d
WHERE ABS(s.revenue_sar - m.revenue_sar) > 0.01
ORDER BY s.d DESC;
