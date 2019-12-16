class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        steps = len(s) // 2
        p1 = 0
        p2 = len(s) - 1

        while steps != 0:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
            steps -= 1
        return s
