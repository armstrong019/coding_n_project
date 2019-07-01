class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if not self.dic.get(number):
            self.dic[number] = 1
        else:
            self.dic[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.dic:
            return False

        for key in self.dic.keys():
            curr_val = key
            other_val = value - key
            if other_val == curr_val:
                if self.dic[key] > 1:
                    return True
            else:
                if other_val in self.dic.keys():
                    return True

        return False

