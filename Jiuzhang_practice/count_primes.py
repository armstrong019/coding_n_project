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
