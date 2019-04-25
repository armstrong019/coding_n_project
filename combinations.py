class Solution:
    """
    comments:
    给出1到n 个数 从中选k个一共有多少种选择。 大致思路是从1。。k一共k个空间， 每一次选一个数填上， 而且后一个要比前一个大（有序的），
    那第一个空一共有n个填法， 第二个空有（n-1）， 第k个空有 （n-k+1）个填法： 具体表现在那个for loop里面。
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        result = []
        self.helper(result, n, k, 1, 0, [])
        return result

    def helper(self, result, n, k, current_value, count, temp):
        if count == k:
            result.append(temp[:])
            return
        for i in range(current_value, n + 1): #这个current value相当于一个指针， 指向当前选定开始值
            temp.append(i)
            self.helper(result, n, k, i + 1, count + 1, temp)
            temp.pop()
