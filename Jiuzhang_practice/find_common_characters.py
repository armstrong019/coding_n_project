from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        nums = Counter(A[0])
        for i in range(1, len(A)):
            nums &= Counter(A[i])
        return list(nums.elements())

#Counter can take the intersect
# use list(nums.elements()) to get the outputpairs