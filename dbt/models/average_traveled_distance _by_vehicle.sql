 {{ config(materialized='view') }}

select
    type,
    avg(traveled_d) as avg_traveled_distance
from
    {{ ref('vehicles') }}
group by
    type;