from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        distance = {start: 1}
        dict.append(end)
        queue = deque([start])
        print(queue)
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
            next_words = self.nextWords(word)
            for w in next_words:
                if w in distance.keys() or w not in dict:
                    continue
                distance[w] = distance[word] + 1
                queue.append(w)
        return 0  # if queue is empty, and yet not find end

    def nextWords(self, word):
        next_words = []
        chars = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(len(word)):
            left_word = word[:i]
            right_word = word[i + 1:]
            for j in chars:
                if j != word[i]:
                    next_words.append(left_word + j + right_word)
        return next_words

x= Solution()
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]


start = "a"
end = "c"
dict=["a","b","c"]
print(x.ladderLength(start, end, dict))