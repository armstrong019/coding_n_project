string = "hello world ok "
# strip 的写法
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        return ' '.join(x[::-1])

# string.split(' ') 根据空格将string切分, 注意这里面空格是deliminator 那么切出来会有空的词
# '  hello  world' -- 切分的结果是 【'','','hello','','world'】
# string.split(): 会将多个空格压缩成一个空格， 并且开头结尾的空格都会被抹去

# pointer 的写法
class Solution:
    def reverseWords(self, s: str) -> str:
        List = []
        p = 0
        while p <= len(s) - 1:
            if s[p] == ' ':
                p += 1
            else:
                word, ind = self.get_word(s, p)
                p = ind
                List.append(word)
        return ' '.join(List[::-1])

    def get_word(self, s, p):
        ind = p
        while ind <= len(s) - 1 and s[ind] != ' ':
            ind += 1
        return s[p:ind], ind
