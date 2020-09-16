# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


# 第一种方法是binary search 把每一行的最小等于1的column number都找到 然后取得最小的
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        nrow, ncol = binaryMatrix.dimensions()
        min_col = ncol + 1 # need to be a large number
        for i in range(nrow):
            # below is standard binary search
            start = 0
            end = ncol - 1
            while start + 1 < end:
                mid = (start + end) // 2
                val = binaryMatrix.get(i, mid)
                if val == 0:
                    start = mid
                else:
                    end = mid
            # 最后结果有三类 start，end 分别对应 （0，0）（0，1）（1，1）
            if binaryMatrix.get(i, start) == 1: # need to check start first
                current_min_col = start
            elif binaryMatrix.get(i, end) == 1:
                current_min_col = end
            else:
                current_min_col = ncol + 1
            min_col = min(current_min_col, min_col)
        if min_col == ncol + 1:
            return -1
        return min_col

# 第二种方法是 cross 格子的方法 基本思路如下：
# 从右上角开始， 如果当前值是1 那么它以下的列的值都可以不用考虑了（因为不可能更好）那么这个时候往左边走
# 如果当前值是0 那么它同行的左边的值都可以不用考虑了（因为不可能更好）那么这个时候往下边走
# 这个思路很直接， 但是要注意row col 不要写反了
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        nrow, ncol = binaryMatrix.dimensions()
        r = 0
        c = ncol - 1
        min_col = sys.maxsize
        while r >= 0 and r <= nrow - 1 and c >= 0 and c <= ncol - 1:
            val = binaryMatrix.get(r, c)
            if val == 1:
                min_col = min(min_col, c)  # 更新最小col的值
                c -= 1  # go to left
            else:
                r += 1  # go down
        if min_col == sys.maxsize:
            return -1
        return min_col



