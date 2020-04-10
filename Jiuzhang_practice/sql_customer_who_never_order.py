select tb1.Name as Customers
from Customers as tb1
left join Orders as tb2
on tb1.Id = tb2.CustomerId
where tb2.Id is null;

# 这里面利用了一个特性就是left join 那么右边那个table 可能没有对应上， 那这个时候就会出现null

