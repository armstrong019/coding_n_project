class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.min_stack == []:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

#
# 使用两个仅支持 pop 和 push 的栈就可以完成, stack 储存压入的数据, minStack 储存最小值.
# push 直接把元素压入 stack, 对于 minStack, 如果它为空则直接压入, 反之压入当前元素与 minStack 栈顶的最小值
# pop 两个栈都弹出一个元素, 返回 stack 弹出的元素
# min 返回 minStack 的栈顶

# 是不是还可以用heap 可以实验一下
import heapq

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.heap[0]: #这个地方比较巧妙 如果pop出去的这个数字不是 最小值， 那么不需要更新heao 否则要更新
            heapq.heappop(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]

