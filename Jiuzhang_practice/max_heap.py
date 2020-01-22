#跟 min stack 相似
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.max_stack == []:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> int:
        val = self.stack.pop()
        self.max_stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        mx = self.max_stack[-1] # 首先找到最大的
        temp = [] # 用一个temporary stack
        while self.stack[-1] != mx:
            temp.append(self.stack.pop()) # 如果不是最大的都push到 temp里面去
            self.max_stack.pop()
        self.stack.pop() # 把最大的值pop 出来
        self.max_stack.pop()
        while temp != []:
            x = temp.pop()
            self.push(x) # 将剩下的值都push进去
        return mx
