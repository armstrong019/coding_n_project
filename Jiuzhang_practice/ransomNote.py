class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """

    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        dic = {}
        for s in ransomNote:
            dic[s] = ransomNote.count(s)
        for s in dic.keys():
            if dic[s] > magazine.count(s):
                return False
        return True
    # 最优做法，计算在ransomNote 里面的frequency， 只要在dic里面足够就好了
