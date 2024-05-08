{{ config(materialized='view') }}

select
    type,
    count(*) as vehicle_count
from
    {{ ref('vehicles') }}
group by
    type;
