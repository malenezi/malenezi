{#
  Map a raw Masar city CODE to the conformed city NAME.

  It exists so the mapping is written once. Six staging models each carrying
  their own CASE expression is six places to update when Masar opens in Mecca,
  and five of them will be updated.

  Usage:  {{ conform_city('city') }} as city
#}
{% macro conform_city(column_name) %}
    case upper(trim({{ column_name }}))
        when 'RUH' then 'Riyadh'
        when 'JED' then 'Jeddah'
        when 'DMM' then 'Dammam'
        when 'MKK' then 'Mecca'
        when 'MED' then 'Medina'
        else initcap(trim({{ column_name }}))
    end
{% endmacro %}
