# Write your MySQL query statement below
select Department,Employee,Salary
from
( select d.name as Department,e.name as Employee,Salary,
dense_rank()over (partition by d.id,d.name
order by salary desc)as sal
from employee e
join department d
on e.departmentid = d.id)x
where sal <=3;
