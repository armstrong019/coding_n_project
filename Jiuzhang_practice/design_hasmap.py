# 最直接的解法
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = [-1]*1000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.container[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.container[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        self.container[key] = -1

# 用二维数组的解法
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = [[-1]*1000 for _ in range(1000)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        i = key //1000
        j = key%1000
        self.container[i][j] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        i = key //1000
        j = key%1000
        return self.container[i][j]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        i = key //1000
        j = key%1000
        self.container[i][j] = -1
