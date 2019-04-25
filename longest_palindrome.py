class Solution:
    """
    comments:这道题用hash table， 记录单双数，如果一个词出现了双数， 那么肯定存在于palindrome里面， 如果的词是单数次， 那么我们将落单的词拿出
    如果反过来想 用hash table 记录所有落单的词，如果存在， 那么最多出现一次。
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here

        hash = {}
        for i in s:
            if i in hash:
                del hash[i]
            else:
                hash[i] = True

        if len(hash) == 0:
            return len(s)
        else:
            return len(s) - len(hash) + 1
