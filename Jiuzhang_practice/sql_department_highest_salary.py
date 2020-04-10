# Write your MySQL query statement below

select
tb2.Name as Department, tb1.Name as Employee, tb1.Salary as Salary

from Employee as tb1
left join Department as tb2
on tb1.DepartmentId=tb2.id
where (tb2.Id, tb1.salary) in (select DepartmentId, max(salary)
                             from Employee
                             group by DepartmentId);

# 这里面有个 XX in table 的用法
