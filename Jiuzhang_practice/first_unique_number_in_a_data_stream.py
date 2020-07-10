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
        # write your code here
        if num in self.hash:
            if self.hash[num] != 0: # hash[nums]
                self.remove(self.hash[num])
                self.hash[num] = 0
            else:
                return
        else:
            # add the new node to the end of the list
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
