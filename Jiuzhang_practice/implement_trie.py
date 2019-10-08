class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
                root = root.children[w] # initerate on root
            else:
                root = root.children[w]
        root.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for w in word:
            print(w)
            if w not in root.children:
                return False
            else:
                root = root.children[w]
        if root.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for w in prefix:
            if w not in root.children:
                return False
            else:
                root = root.children[w]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
print(param_2)
print(obj.root.children['a'].children['p'].children['p'].children)

# Trie Node has two attributes
#1. children: initially is empty dict, as we insert, this became a dictionary with child name: child TireNode object
#             名字和名字对应的那个Node， dictionary 这个structure比较好理解， 主要是找对应关系
#             那么为什么需要node？ 因为我们需要封装， 否则关系混乱
#2. is_word: whether at the level all the node above form a word. Initally is False
