class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p0= m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p0] = nums1[p1]
                p0-=1
                p1-=1
            else:
                nums1[p0] = nums2[p2]
                p0-=1
                p2-=1
        if p1<0:
            nums1[:p0+1] = nums2[:p2+1]
# time complexity is O(m+n), space complexity is O(1)
# 三个指针， 两个分别指向array的最后一位， 第三个指向最后一个0的位置p0，然后进行比较。 将较大的一个放在p0的位置。
# 然后移动指针。
# 最后的情况： 如果p2先为0， 那么数组已经排序好了， 如果p1 先为0， 那么需要把nums2 还没有visited的那几个点移到第一个string里面
