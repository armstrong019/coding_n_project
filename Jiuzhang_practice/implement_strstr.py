class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if len(target)>len(source):
            return -1
        for i in range(0,len(source)-len(target)+1):
            if source[i:i+len(target)]==target:
                return i
        return -1