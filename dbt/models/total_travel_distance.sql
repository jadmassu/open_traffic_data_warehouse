 {{ config(materialized='view') }}

select
    track_id,
    sum(traveled_d) as total_traveled_distance
from
    {{ ref('vehicles') }}
group by
    track_id;