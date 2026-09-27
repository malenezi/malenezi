{#
  The Asia/Riyadh business date for a UTC timestamp.

  Storage is UTC; the business runs on +03. Every "daily" aggregate must use
  this macro, or a trip at 01:30 Riyadh time lands on the previous day's
  report and the daily revenue numbers never quite tie out.

  Usage:  {{ riyadh_business_date('pickup_ts') }} as trip_date
#}
{% macro riyadh_business_date(ts_column) %}
    to_date(from_utc_timestamp({{ ts_column }}, 'Asia/Riyadh'))
{% endmacro %}
