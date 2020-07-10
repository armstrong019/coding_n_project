# 这道题细节最多， 比较麻烦， 但是algorithm不难
# 用DLL记录已经出现的query， 这里我定义了两个dummy， head和tail 这样相对简单， 不需要update tail 和head
# hashtable 记录两个东西，key 是 put function 的key，value 是一个tuple（value，node）-- node是在DLL里面的node
# 新的点在 tail of LL，旧的点在head of LL

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.hash = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            node = self.hash[key][1]
            val = self.hash[key][0]
            self.move_to_end(node)
            return val

    def __remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None

    def __add_to_end(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def move_to_end(self, node):
        self.__remove_node(node)
        self.__add_to_end(node)
        # no need update hash, still same obj

    def remove_from_head(self):
        remove_node = self.head.next
        key = remove_node.value
        self.head.next = remove_node.next
        remove_node.next.prev = self.head
        remove_node.next, remove_node.next = None, None
        return key # return the key of the node removed to update hash

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            if len(self.hash) == self.capacity:
                key0 = self.remove_from_head() # key0 不一样
                del self.hash[key0]
            NewNode = Node(key)
            self.__add_to_end(NewNode)
            self.hash[key] = (value, NewNode)
        else:
            node = self.hash[key][1]
            self.move_to_end(node)
            self.hash[key] = (value, node)

