

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while (x != 0 or y != 0): # 注意这里面的条件 当或y两个里面的一个不为0
            if x % 2 != y % 2:
                dist += 1
            x = x // 2
            y = y // 2
        return dist

