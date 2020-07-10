# cross join
SELECT
      a.Name AS 'Employee'
From Employee As a, Employee As b
WHERE a.ManagerId = b.Id AND a.Salary>b.Salary;


# left join
select a.Name as Employee
from Employee as a
left join Employee as b
on a.ManagerId = b.Id
where b.Id is not null and a.Salary>b.Salary;

