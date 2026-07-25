# Write your MySQL query statement below
select s.user_id,ifnull(round(count(case when action = "confirmed" then 1 end)/count(c.action),2),0) as confirmation_rate
from Signups s
left join confirmations c
on s.user_id  = c.user_id
group by s.user_id;

;
