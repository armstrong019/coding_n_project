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


# 下面是window function的写法。
# 两点： 一点是alias 起名字不能用built in operation的名字 所以叫 rnk 不叫rank
# 第二点是注意departmnet Id 不存在的corner case
select t1.Department, t1.Employee, t1.Salary
from
(select d.Name as Department, e.Name as Employee, e.Salary, Rank() over (partition by d.Name order by Salary Desc) as rnk
from Employee as e
left join Department as d
on e.DepartmentId = d.Id) as t1
where rnk=1 and t1.Department is not null;


