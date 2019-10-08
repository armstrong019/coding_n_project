class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]
            else:
                if s_dict[s[i]]!= t[i]:
                    return False
            if t[i] not in t_dict:
                t_dict[t[i]] = s[i]
            else:
                if t_dict[t[i]]!= s[i]:
                    return False
        return True

 # example： s='ab', t ='aa' False
 #           s='ab', t='ca' True
 # 这个例子比较绕。 用两个字典做比较容易。如果s对于t 是iso的那么他对于s 一定也是ISO的。 那么两个字典的功能应该是对等的/
