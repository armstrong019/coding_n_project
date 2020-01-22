# 罗马文 写成integer
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        i = 0
        num = 0
        while i <= len(s)-1:
            if i+1<=len(s)-1 and dic[s[i]]<dic[s[i+1]]: # 如果后一位的值比前一位的大， 那么实际上它属于特殊情况 比如 4， 9， 40，90 的情况
                num += dic[s[i+1]]-dic[s[i]]
                i += 2
            else:
                num += dic[s[i]]
                i+=1
        return num
