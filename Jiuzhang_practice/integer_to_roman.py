# 以下为两种不同的写法。 第二种写法更优， 第一种更直接。
class Solution:
    def intToRoman(self, num: int) -> str:
        # 从大到小排列字符
        dict_ = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                 5: 'V', 4: 'IV', 1: 'I'}

        str_ = ''
        while num > 0:
            for n, roman in dict_.items():
                if num - n >= 0: # 如果当前的数比字典里的其中一个数大
                    str_ += roman # 那么就减去这个数，同时写出这个数对应的字符
                    num = num - n
                    break # 做完以上操作要跳出loop 从新来过， 不能再继续for loop
                else:
                    continue
        return str_


class Solution:
    def intToRoman(self, num: int) -> str:
        dict_ = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                 5: 'V', 4: 'IV', 1: 'I'}

        str_ = ''
        for n, roman in dict_.items():
            while num - n >= 0: # while 的写法相当简洁
                str_ += roman
                num = num - n
        return str_
