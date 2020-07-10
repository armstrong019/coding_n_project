
select Id, Month as month, sum(Salary) over (partition by Id order by Month ROWS 2 preceding) as Salary
from Employee
where (Id, Month) not in (select Id, max(Month) from Employee group by Id)
order by Id ASC, Month Desc

# ROWS preceding 2 是指用前面两行和当前一行的三个数值apply操作
# ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
# partition by 是指将将数据分区， 没有的话就不分区
# order by 是用来apply rolling function， 没有的话就不apply rolling operation
#
