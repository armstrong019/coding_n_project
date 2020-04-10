Select
(SELECT DISTINCT
    Salary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary


# 如果像下面这样写在table 为空的时候会报错，
select distinct t1.salary as SecondHighestSalary
from (select Salary from Employee order by Salary desc) as t1
limit 1
offset 1;
