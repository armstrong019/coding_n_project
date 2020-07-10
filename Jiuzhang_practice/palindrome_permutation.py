class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        dic = {}
        for letter in s:
            if letter in dic:
                del dic[letter]
            else:
                dic[letter] = 1
        return len(dic)<=1

