# 第一个不重复的数字，跟LRU cache 一样 需要用到double linked list
# use a hash to remember this: key: the number, value: the ListNode if the number is seen only once,
# the second time we see the same number, we change its value in hash to 0 (防止同一个点被delete很多次)
# use DLL 去记录当前的没有重复的数字 （按照先后顺序，先出现的靠近头部，后出现的靠近尾部）

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# hash 代表
class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.hash = {}  # 记录node 的val何其对应的node，只要出现过就要记录
        self.head = Node(-1)  # 需要head牵出整个list 并且在firstUnique 的时候进行判断
        self.tail = self.head  # 需要tail 因为删除tail的时候和删除中间节点是不一样的

    def add(self, num):
        if num in self.hash: # 如果数字已经出现过了，
            if self.hash[num] != 0: # hash[nums] 不等于0 说明该数字在这次之前只出现过一次， 那么还在DLL里面
                node = self.hash[num]
                self.remove(node) # 将node从DLL里面去除
                self.hash[num] = 0 # hash 里面标注为0
            else:
                return # 如果self.hash[num] == 0 说明已经出现多次， 那么DLL里面已经没有该node了， 这时候不用delete
        else:
            # 如果数字没有出现， add the new node to the end of the list， update tail and hash
            new_node = Node(num, self.tail, None)
            self.tail.next = new_node
            self.hash[num] = new_node
            self.tail = new_node

    def remove(self, node):
        # need to care about case that the node is the tail
        if node == self.tail:
            node.prev.next = node.next
            self.tail = self.tail.prev  # need to redefine tail
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # node.prev, node.next = None, None #有没有都行

    def firstUnique(self):
        # write your code here
        if self.head.next is None:
            return -1
        return self.head.next.val

# brute force 的写法
from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        dic = defaultdict(int)
        for letter in s:
            dic[letter] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
