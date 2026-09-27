-- Staging: 1:1 with bronze.drivers. hire_date arrives in MIXED formats on
-- purpose — three of them, all real, all seen in the source.
{{ config(materialized='view') }}

with source as (

    select * from {{ source('bronze', 'drivers') }}

),

deduped as (

    -- Bronze is append-only and the roster is re-landed daily, so keep the
    -- most recently landed row per driver.
    select * from (
        select
            *,
            row_number() over (
                partition by driver_id
                order by _ingested_at desc, _batch_id desc
            ) as _rn
        from source
    )
    where _rn = 1

),

parsed as (

    select
        cast(driver_id    as string)  as driver_id,
        cast(full_name_en as string)  as full_name_en,     -- PDPL: personal data
        case upper(trim(city))
            when 'RUH' then 'Riyadh'
            when 'JED' then 'Jeddah'
            when 'DMM' then 'Dammam'
            when 'MKK' then 'Mecca'
            when 'MED' then 'Medina'
            else initcap(trim(city))
        end                           as city,

        -- Three OBSERVED formats. Add a branch only for a format you have
        -- actually seen: an unused branch that later matches the wrong string
        -- is worse than a null you can detect.
        coalesce(
            to_date(hire_date, 'yyyy-MM-dd'),
            to_date(hire_date, 'dd/MM/yyyy'),
            to_date(hire_date, 'MMM d, yyyy')
        )                             as hire_date,

        cast(rating as double)        as rating,
        lower(trim(status))           as status,
        cast(national_id_hash as string) as national_id_hash,  -- PDPL: pseudonymised, never re-identify
        cast(phone_hash       as string) as phone_hash,        -- PDPL: pseudonymised
        _batch_id,
        _ingested_at

    from deduped
    where driver_id is not null

)

select * from parsed
