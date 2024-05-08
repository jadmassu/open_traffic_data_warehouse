 {{ config(materialized='view') }}
select
    type,
    avg(avg_speed) as avg_speed
from
    {{ ref('vehicles') }}
group by
    type