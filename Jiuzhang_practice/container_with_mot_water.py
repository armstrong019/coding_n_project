class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        cur=max_area=0
        while i!=j:
            if height[i]<=height[j]:
                cur=height[i]*(j-i)
                max_area=max(cur,max_area)
                i+=1
            else:
                cur=height[j]*(j-i)
                max_area=max(cur,max_area)
                j-=1
        return max_area