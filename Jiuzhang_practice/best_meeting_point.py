class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x_location = []
        y_location = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_location.append(i)
                    y_location.append(j)
        return self.medium_dist(x_location) + self.medium_dist(y_location)

    def medium_dist(self, L):
        L.sort()
        m = len(L) // 2
        total_dist = 0
        for i in range(len(L)):
            total_dist += abs(L[i] - L[m])
        return total_dist
# 这道题也是考察逻辑。 best meeting point 就是所有点的中位数。
