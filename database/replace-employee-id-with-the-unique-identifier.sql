# Write your MySQL query statement below
select unique_id,name
from employees e
left join employeeUni eu
on e.id = eu.id;