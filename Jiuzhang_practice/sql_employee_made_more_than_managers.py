SELECT
      a.Name AS 'Employee'
From Employee As a, Employee As b
WHERE a.ManagerId = b.Id AND a.Salary>b.Salary;

# another cross join example
