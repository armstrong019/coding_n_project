from collections import deque


class MyQueue:
    def __init__(self):
        # do intialization if necessary
        self.s1 = deque([])
        self.s2 = deque([])

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if self.s2:
            x = self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            x = self.s2.pop()
        return x

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if self.s2:
            x = self.s2[-1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            x = self.s2[-1]
        return x
# 放的时候就往1里面放，
# pop的时候是这样： 从2里面拿（最后一个位置）， 如果2里面没有 1里面有， 就将1里面的挪到2里去