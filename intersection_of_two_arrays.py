class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        x = set(nums1)
        y = set(nums2)
        z = x.intersection(y)
        return list(z)

# z = [i for i in x if x in y]