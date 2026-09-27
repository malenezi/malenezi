{{ config(materialized='table', file_format='delta', alias='dim_date') }}
-- gold.dim_date — GRAIN: one row per calendar date.
--
-- THE conformed date dimension. There is exactly one of these in the platform,
-- forever. Two date dimensions is how the revenue dashboard and the demand
-- dashboard start disagreeing about what "last week" means.
with spine as (
    select explode(sequence(date('2026-01-01'), date('2026-12-31'), interval 1 day)) as full_date
)
select
    cast(date_format(full_date, 'yyyyMMdd') as int)      as date_key,
    full_date,
    year(full_date)                                      as year,
    quarter(full_date)                                   as quarter,
    month(full_date)                                     as month,
    date_format(full_date, 'MMMM')                       as month_name_en,
    day(full_date)                                       as day_of_month,
    dayofweek(full_date)                                 as day_of_week,
    date_format(full_date, 'EEEE')                       as day_name_en,
    -- KSA working week is Sunday..Thursday, so the WEEKEND is Friday+Saturday
    -- (dayofweek 6 and 7 in Spark's 1=Sunday numbering). Getting this wrong
    -- silently shifts every "weekend demand" analysis by two days — and it
    -- looks plausible, which is why nobody catches it.
    case when dayofweek(full_date) in (6, 7) then true else false end as is_weekend,
    weekofyear(full_date)                                as week_of_year
from spine
