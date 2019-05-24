class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        counter = {}
        for s in str:
            if s not in counter.keys():
                counter[s]=1
            else:
                counter[s]+=1
        for s in str: # 顺序是由序列记录的
            if counter[s]==1:
                return s
        return None
