from collections import deque
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.cache = deque([])
        self.size = size
        self.sum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.cache) < self.size:
            self.cache.append(val)
            self.sum += val
        else:
            x = self.cache.popleft()
            self.cache.append(val)
            self.sum = self.sum-x+val
        return self.sum/len(self.cache)

# 这道题就是要用一个cache来keep一个list的长度
# 然后用一个variable sum来记录总和的值--如果没有这个容易超时。