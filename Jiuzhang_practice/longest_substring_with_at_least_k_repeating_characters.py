# brute force 这种方法超时了
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        maxn = 0
        for i in range(len(s)-1):
            dic = {s[i]:1}
            for j in range(i+1, len(s)):
                if s[j] in dic:
                    dic[s[j]]+=1
                else:
                    dic[s[j]]=1
                if all([n>=k for n in dic.values()]):
                    if j-i+1>maxn:
                        maxn= j-i+1
        return maxn

# divide and conquer:
class Solution:
    def longestSubstring(self, s, k):
                dic = {}
                for letter in s:
                    if letter in dic:
                        dic[letter] += 1
                    else:
                        dic[letter] = 1
                for letter in s:
                    if dic[letter] < k:
                        lists = s.split(letter)
                        res = []
                        for list in lists:
                            if list == '':
                                res.append(0)
                            else:
                                x = self.longestSubstring(list, k)
                                res.append(x)
                        return max(res)
                return len(s)



