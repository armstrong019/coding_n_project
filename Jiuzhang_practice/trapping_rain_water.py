class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mlh = []
        temp = 0
        for i in range(len(height)):
            mlh.append(temp)
            if height[i]>temp:
                temp = height[i]
        mrh = []
        temp = 0
        height0 = height[::-1]
        for i in range(len(height0)):
            mrh.append(temp)
            if height0[i]>temp:
                temp = height0[i]
        mrh = mrh[::-1]
        mh = [min(mlh[i],mrh[i]) for i in range(len(height))]
        water = 0
        for i in range(len(height)):
            if height[i]<mh[i]:
                water += mh[i]-height[i]
        return water




height = [0,1,0,2,1,0,1,3,2,1,2,1]
x = Solution()
print(x.trap(height))
# 这道题主要就是理解题意，考虑在一个点如何计算水量
