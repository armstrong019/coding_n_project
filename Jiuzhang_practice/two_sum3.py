"""
607. Two Sum III - Data structure design
中文English
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.count = {}

    def add(self, number):
        # write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for number in self.count:
            if value - number != number and value - number in self.count:
                return True
            if value - number == number and self.count[number] > 1:
                return True
        return False

#using a hashtable, record the frequency of the occurance
# be careful about how to handle case of value = number*2 