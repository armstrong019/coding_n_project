# 直接的做法
import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        temp = head
        i = 0
        while temp is not None:
            i+=1
            temp = temp.next
        self.len = i   # 找到list的长度


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        steps = random.randint(0, self.len-1) # 随机抽取一个
        temp = self.head
        for i in range(steps):
            temp=temp.next
        return temp.val

# 这道题我们同时可以用reservior sampling 去做
# 参见random pick index
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 0
        temp = self.head
        while temp:
            if random.randint(0,count)==0:
                res = temp.val
            temp = temp.next
            count+=1
        return res
