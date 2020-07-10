class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort(reverse=True)
        n = len(citations)
        start = 0
        end = n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if mid >= citations[mid]:
                end = mid
            else:
                start = mid

        if start >= citations[start]:
            return start
        if end >= citations[end]:
            return end

        return len(citations)
