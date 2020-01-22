# 类似于spiral1 还是要用数学计算。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        res = [[0 for _ in range(n)] for _ in range(n)]
        res[0] = [x for x in range(1, n+1)]
        dirs = [[1,0],[0,-1],[-1,0],[0,1]]
        steps = [n-1,n-1,n-2,n-2]
        x,y,val=0, n-1,n
        counter = n**2-n
        k =0
        while counter>0:
            dir = dirs[k]
            step = steps[k]
            for m in range(step):
                x = x+dir[0]
                y = y+dir[1]
                res[x][y] = val+1
                val +=1
                counter -= 1
            steps[k] = steps[k]-2
            k = (k+1) %4
        return res
