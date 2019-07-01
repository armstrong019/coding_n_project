class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        v1 = [int(x) for x in v1]
        v2 = [int(x) for x in v2]
        n = max(len(v1), len(v2))
        diff = abs(len(v1) - len(v2))
        if len(v1) > len(v2):
            v2 = v2 + [0 for _ in range(diff)]
        if len(v1) < len(v2):
            v1 = v1 + [0 for _ in range(diff)]

        for i in range(n):
            if v1[i] == v2[i]:
                continue
            if v1[i] > v2[i]:
                return 1
            if v1[i] < v2[i]:
                return -1
        return 0

# this question is more about data preprocessing
