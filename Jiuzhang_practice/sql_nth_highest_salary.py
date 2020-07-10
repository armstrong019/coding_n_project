CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N = N - 1;
RETURN(
    # Write your MySQL query statement below.
    select distinct Salary
    from Employee
    order by Salary Desc
    limit 1 offset N  # limit 表示输出的个数， offset表示 措出的个数
);
END




# Limit and offset
# * When you only need a query to return a certain number of entries, you can use LIMIT clause to set that limitation.
# * If you want the query to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start.

# 用window function的做法
# 注意这里面必须要用sub query，
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN(
    # Write your MySQL query statement below.
    select distinct A.salary
    from
        (select salary, dense_rank() over(order by Salary DESC) as rnk
        from Employee) as A
    where A.rnk = N
);
END

错误写法： 因为首先要计算rank， 然后才能进行where拣选， 因为where 语句的顺序发生在select 之前， 所以说where 发生的时候是没有rnk 值的
select salary, dense_rank() over(order by Salary DESC) as rnk
from Employee
where rnk=2;
