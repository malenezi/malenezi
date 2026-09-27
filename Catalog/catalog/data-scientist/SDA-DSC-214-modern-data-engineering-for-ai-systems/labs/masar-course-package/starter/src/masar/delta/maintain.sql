-- src/masar/delta/maintain.sql — the same maintenance, as SQL you can read.
-- Run nightly (masar.delta.maintain does this from the DAG); run by hand the
-- first time so you SEE the numbers change.

-- 0) Baseline: record numFiles and sizeInBytes BEFORE anything.
DESCRIBE DETAIL delta.`./lakehouse/silver/trips`;

-- 1) Compact small files and cluster by the columns queries filter on.
--    ZORDER co-locates related rows so min/max statistics prune more rows.
OPTIMIZE delta.`./lakehouse/silver/trips`
  ZORDER BY (city, pickup_ts);

-- 2) Verify: file count should drop sharply, average file size should rise.
DESCRIBE DETAIL delta.`./lakehouse/silver/trips`;

-- 3) What WOULD be deleted, without deleting it. Always run this first.
VACUUM delta.`./lakehouse/silver/trips` RETAIN 168 HOURS DRY RUN;

-- 4) Reclaim storage older than the retention window.
--    RETENTION IS A GOVERNANCE DECISION: 168h keeps 7 days of time travel.
--    Do NOT set 0 hours: it destroys audit history and can break readers
--    that are mid-query against a version you just removed.
VACUUM delta.`./lakehouse/silver/trips` RETAIN 168 HOURS;
