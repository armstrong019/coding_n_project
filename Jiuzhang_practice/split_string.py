class Solution:
    """
    dfs+backtrack, result generate in place.
    dfs function input: result, current path (from start to currentrom start to current),), current string s (s not being considered)
        function output: result
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        result = []
        self.dfs(result, [], s)
        return result

    def dfs(self, result, temp, s):
        if s == "":
            result.append(temp[:])  # deep copy path
            return

        for i in range(2):
            if i + 1 <= len(s):  # prevent multiple same input, index slicing can go out of range
                temp.append(s[:i + 1]) #s[1:] or s[2:]
                self.dfs(result, temp, s[i + 1:])
                temp.pop()

