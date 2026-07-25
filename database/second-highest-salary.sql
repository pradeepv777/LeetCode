# Write your MySQL query statement below
select Max(salary) as SecondHighestSalary
from(
    select salary,dense_rank() over (order by salary desc)
    as Sec
    from Employee)x
    where Sec = 2;
