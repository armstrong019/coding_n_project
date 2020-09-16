class Trie:
    def __init__(self):
        self._trie = {}

    def addWord(self, word):
        curr = self._trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = word

    @property
    def gettrie(self):
        return self._trie


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        trie = self.createTrie(words)
        self.ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.gettrie:
                    self.wordSearchDFS(i, j, trie.gettrie, set())
        return self.ans

    def createTrie(self, words):
        trie = Trie()
        for word in words:
            trie.addWord(word)
        return trie

    def wordSearchDFS(self, i, j, curr, visited):
        visited.add((i, j))
        if '*' in curr[self.board[i][j]]:
            self.ans.add(curr[self.board[i][j]]['*'])
        currletter = self.board[i][j]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        desired = curr[currletter]
        for x, y in directions:
            dx = i + x
            dy = j + y
            if dx >= 0 and dx < len(self.board) and dy >= 0 and dy < len(self.board[0]):
                if self.board[dx][dy] in desired and (dx, dy) not in visited:
                    self.wordSearchDFS(dx, dy, desired, visited)
        visited.remove((i, j))
