# Write your MySQL query statement below
select query_name,round(AVG(rating * 1.0 / position), 2) AS quality,round(COUNT(CASE WHEN rating < 3 THEN 1 END) * 100 / COUNT(*), 2)
as poor_query_percentage
from Queries
group by query_name
;