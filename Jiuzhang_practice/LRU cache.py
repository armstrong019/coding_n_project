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


# 另外一种写法，只是定义了一个dummy head 这时候要注意update tail（没有上边好写）

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1)
        self.tail = self.head
        self.hash = {}  # key: (node, val)

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            node, val = self.hash[key]
            _ = self.delete_node(node)  # delete node
            self.append_node_to_end(node)  # do not need to update hash
            return val

    def delete_node(self, node):
        if node == self.tail:  # end of the list
            self.tail = node.prev
            node.prev.next = None
            node.prev = None
            node.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
        return node.key

    def append_node_to_end(self, node):
        self.tail.next = node  # move node to end of list
        node.prev = self.tail
        self.tail = node  # redefine tail

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            new_node = Node(key)
            if len(self.hash) < self.capacity:
                self.append_node_to_end(new_node)
                self.hash[key] = (new_node, value)
            else:
                self.append_node_to_end(new_node)
                node_to_delete = self.head.next
                key0 = self.delete_node(node_to_delete)
                self.hash[key] = (new_node, value)
                del self.hash[key0]
        else:  # if key already in hash
            node = self.hash[key][0]
            _ = self.delete_node(node)  # delete node
            self.append_node_to_end(node)
            self.hash[key] = (node, value)

