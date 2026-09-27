-- Reconciliation: the demand mart's trip count must equal silver's, for the
-- days the mart covers. If these disagree, one dashboard is wrong and nobody
-- knows which — the exact failure the "reporting divergence" case study is
-- about.
with mart as (
    select demand_date as d, sum(trips) as mart_trips
    from {{ ref('gold_zone_hourly_demand') }}
    group by demand_date
),
silver as (
    select to_date(pickup_ts) as d, count(*) as silver_trips
    from {{ ref('silver_trips') }}
    where status = 'completed'
    group by to_date(pickup_ts)
)
select m.d, m.mart_trips, s.silver_trips
from mart m
join silver s on m.d = s.d
where m.mart_trips <> s.silver_trips
