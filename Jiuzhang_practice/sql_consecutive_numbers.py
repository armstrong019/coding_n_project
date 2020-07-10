# Write your MySQL query statement below
select DISTINCT
    l1.Num AS ConsecutiveNums
from Logs as l1
cross join Logs as l2
cross join logs as l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num;
