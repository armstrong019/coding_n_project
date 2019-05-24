class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        str0 = teststr.split(" ")
        word_dict = {}
        for ind, i in enumerate(pattern):
            if i in word_dict:
                if word_dict[i] != str0[ind]:
                    return False
            else:
                if str0[ind] in word_dict.values():
                    return False
                word_dict[i] = str0[ind]
        return True

# using hashtable
# two scenarios:
# 1. when we a pattern is already seen, need to make sure the pattern and word is matched
# 2. when a pattern is not seen, need to make sure the word have not appeared before