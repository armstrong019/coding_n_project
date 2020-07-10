# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# 注意这个是比N小的数字， 所以考虑 0，1，2，。。。N-1， 第一个0 其实不用考虑， 但是在indexing上从0 开始比较方便。
# 这个就是用到那个比较著名的algorthm
# 从2 到N-1那样缕，
# 2 是第一个prime，然后 2 的倍数都不是prime
# 3 是下一个prime，（因为3 不是 比他小的prime的倍数（没划掉）， 所以3一定是prime）， 3 的倍数都不是prime，
# 注意这时候倍数可以 从 3*3， 3*4 算起， 因为3*2 已经被划掉了

# 优化写法
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        is_prime =[True for i in range(n)]
        is_prime[:2]=[False, False]
        for p in range(2,n):
            if is_prime[p]:
                j=p
                while p*j<n: # 如果当前是prime， 把后面的乘数都set 成 不是prime
                    is_prime[p*j]=False
                    j+=1
        return sum(is_prime)

# time limit exceed
# 这版本是我自己写的， 面试好使 O（n^2）
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        List = [2]
        count = 1
        for i in range(2, n):
            is_prime = True
            for number in List:
                if i % number == 0:
                    is_prime = False
                    break
            if is_prime:
                List.append(i)
                count += 1
        return (count)
