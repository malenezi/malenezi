-- A trip cannot end in the future. This catches timezone drift (a
-- to_utc_timestamp applied twice, or not at all) and bad source clocks —
-- both of which produce data that passes every column-level test.
--
-- A singular test returns the OFFENDING ROWS; zero rows means it passed.
select
    trip_id,
    pickup_ts,
    dropoff_ts
from {{ ref('silver_trips') }}
where dropoff_ts > current_timestamp() + interval 1 hour
