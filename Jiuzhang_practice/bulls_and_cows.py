# the first version is slow, since it loop 3 times
from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_bulls = 0
        bull_index = []
        # first take care of the bulls:
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                num_bulls += 1
                bull_index.append(i)

        s_dict = defaultdict(list)
        for i in range(len(secret)):
            if i not in bull_index:
                s_dict[secret[i]].append(i)

        num_cows = 0
        # now take care of the cows
        for i in range(len(secret)):
            if i not in bull_index:
                if guess[i] in s_dict:
                    if s_dict[guess[i]] != []:
                        s_dict[guess[i]].pop()
                        num_cows += 1

        return ''.join([str(num_bulls), 'A', str(num_cows), 'B'])

# the 2nd version is an optimized version
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # another approach is to use counter
        num_bulls = 0
        num_cows = 0
        s_dic = defaultdict(int)
        g_dic = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]: # this is a bull
                num_bulls += 1
            else:
                s_dic[secret[i]] +=1 # use dict to record the number of occurence of each word that is not bull
                g_dic[guess[i]] += 1

        for g in g_dic:
            if g in s_dic:
                num_cows += min(g_dic[g], s_dic[g]) # the minimum of these two is the num of cows for word g
        return str(num_bulls) + 'A' + str(num_cows) + 'B'
