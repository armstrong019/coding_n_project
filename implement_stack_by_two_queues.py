from collections import deque


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])
    def push(self, x):
        # write your code here
        self.q1.append(x)
        print(self.q1, self.q2)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if not self.q1:
            return None
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        x = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.q1:
            return None
        while len(self.q1)>1:
            self.q2.append(self.q1.popleft())
        x = self.q1.popleft()
        self.q2.append(x)
        self.q1, self.q2 = self.q2, self.q1
        return x
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if not self.q1:
            return True
        else:
            return False


# 两个queue， 加的时候就往第一个里面加，
# pop 时候： 将第一个里面的放到第二个queue里面 一直到第一个里面只剩下一个， 将它pop出来， 然后将两个queue 互换
# top 时候： 和pop一样， 但是要记住看完之后要放回去
