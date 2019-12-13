class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0

        while n >= 5:
            q = n // 5
            zeros += q
            n = q

        return zeros
#
# 这道题并没有什么难度，是让求一个数的阶乘末尾0的个数，也就是要找乘数中 10 的个数，而 10 可分解为2和5，而2的数量又远大于5的数量
# （比如1到 10 中有2个5，5个2），那么此题即便为找出5的个数。仍需注意的一点就是，像 25，125，这样的不只含有一个5的数字需要考虑进去
