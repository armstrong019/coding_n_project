# 这个是更新的一版。这里要求找出来的result 必须要从大到小排列
# 下面我写两个版本，第一个版本很直接，
# 用bisect，找到 和 x 最接近的值应该存在于 ind-1，ind 之间
# 然后开始以ind-1 和ind 为中心继续想外找
# 找到之后 将result append 上去， 然后将result sort了 输出
from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        ind = bisect(arr, x)
        if ind == 0:
            return arr[0:k]
        elif ind == len(arr):
            temp = arr[len(arr) - k:len(arr)]
            return temp
        else:

            left = ind - 1
            right = ind
            print(left, right)
            result = []
            while left >= 0 and right <= len(arr) - 1 and len(result) < k:
                if abs(x - arr[left]) <= abs(x - arr[right]):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            if len(result) != k:
                while len(result) < k and left >= 0:
                    result.append(arr[left])
                    left -= 1

                while len(result) < k and right <= len(arr) - 1:
                    result.append(arr[right])
                    right += 1
            return sorted(result)

# 第二个版本思路一致， 不需要sort 最后的结果 只需要找到left 和right 的边界就好。
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        ind = bisect(arr, x)
        if ind == 0:
            return arr[:k]
        elif ind == len(arr):
            return arr[-k:]
        else:
            left = ind - 1
            right = ind
            count = 0
            while left >= 0 and right <= len(arr) - 1 and count < k:
                if abs(x - arr[left]) <= abs(x - arr[right]):
                    left -= 1
                else:
                    right += 1
                count += 1
            if count != k:
                while count < k and left >= 0:
                    left -= 1
                    count += 1

                while count < k and right <= len(arr) - 1:
                    right += 1
                    count += 1

            return arr[left + 1:right] # 最后得到的index是 left+1， left+2，。。。right-1




