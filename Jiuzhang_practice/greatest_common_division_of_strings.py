# 先找到小一点的那个string， 然后将string 拆分 str【i：】 for i in range(len(str))
# 首先看找到的substring 在它自己内部是否满足条件， 然后再看在另一个string里面是否满足条件。
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "" or str2 == "":
            return ""

        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)

        for i in range(len(str1)):
            is_valid_in_itself = self.is_valid_substring(str1[i:], str1) # 注意这里面str1【i：】的长度是由大到小的。所以第一个满足条件的就是答案
            if is_valid_in_itself:
                is_valid = self.is_valid_substring(str1[i:], str2) # 这时候看在str2 是否valid
                if is_valid:
                    return str1[i:]
        return ""

    def is_valid_substring(self, substring, string):
        if len(string) % len(substring) == 0:
            copies = len(string) // len(substring)
            if copies * substring == string:
                return True
        return False

# revisited May 9th， 思路和上面基本一致， 就是执行顺序略有不同
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)
        gcd_str1 = self.gcd(str1)
        for gcd_candidate in gcd_str1:
            # print(str2, gcd_candidate)
            if self.is_gcd(str2, gcd_candidate):
                return gcd_candidate
        return ""

    def gcd(self, str0):
        gcd_list = []
        lenth = len(str0)
        for i in range(len(str0)):
            if self.is_gcd(str0, str0[i:]):
                gcd_list.append(str0[i:])
        return gcd_list

    def is_gcd(self, str0, substring):
        # print(str0, substring)
        lenth = len(str0)
        if lenth % len(substring) == 0:
            times = lenth // len(substring)
            if substring * times == str0:
                return True
        return False

# 这种方法是基于数学的方法。比较巧 面试的时候不一定能想到。 如果str1 + str2 = str2 + str1 那么一定有gcd
class Solution:
    def gcdOfStrings(self, str1, str2):
        # make sure that str1 and str2 must have `Greatest Common Divisor`
        if str1 + str2 != str2 + str1:
            return ''
        # so str1 = nT, str2 = mT
        # T is the Greatest Common Divisor of str1, str2
        sz1 = len(str1)
        sz2 = len(str2)

        while sz1 != sz2:
            if sz1 > sz2:
                sz1 -= sz2
            else:
                sz2 -= sz1

        return str1[:sz1]

# 5 * 7， 5 * 3 = 35，15 - -20，15 - -5，15 - -5，10 - -5，5
