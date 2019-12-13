from collections import deque


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        if end not in dict:
            return 0
        distance = {start:1}
        queue = deque([start])
        while queue:
            curr_word = queue.popleft()
            next_words = self.next_words_gen(curr_word)
            for w in next_words:
                if w == end:
                    return distance[curr_word]+1
                if w in distance or w not in dict:
                    continue
                else:
                    distance[w] = distance[curr_word]+1
                    queue.append(w)
        return 0
    def next_words_gen(self, curr_word):
        next_words = []
        chars = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(len(curr_word)):
            left = curr_word[:i]
            right = curr_word[i+1:]
            for l in chars:
                if l != curr_word[i]:
                    next_words.append(left+l+right)
        return next_words











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
        # this session is used to generate next words with exactly one letter different
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
dict = ["hot","dot","dog","lot","log",'cog']

#
# start = "a"
# end = "c"
# dict=["a","b","c"]
print(x.ladderLength(start, end, dict))
