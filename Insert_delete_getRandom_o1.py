import random

class RandomizedSet:
    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.position = {}
        self.count = 0

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        # write your code here
        self.nums.append(val)
        self.position[val] = self.count
        self.count += 1

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        # write your code here
        if val not in self.position.keys():
            return False
        ind = self.position[val]
        end_pos = ind
        last_element = self.nums[-1]
        self.position[last_element] = end_pos
        del self.position[val]
        self.nums[ind], self.nums[-1] = self.nums[-1], self.nums[ind]
        self.nums.pop()
        self.count -= 1

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        # write your code here
        if not self.nums:
            return []
        return self.nums[random.randint(0, len(self.nums) - 1)]

#这道题如果只有add remove 的function 用hastable 就可以了
# 因为有getRandom 还需要一个list
# 对于hash——table的具体操作是要将要删除的数字的index 找出来， 然后把这个index 给到最后一个数字上， 然后把这个数字从哈希表里删除。