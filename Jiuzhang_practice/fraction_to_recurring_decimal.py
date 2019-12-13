class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # take care of the positive and negative:
        if (numerator<0 and denominator>0) or (numerator>0 and denominator<0):
            res = "-"
        else:
            res = ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        # begin of calculation
        val = numerator // denominator
        residual = numerator % denominator
        res += str(val) # res account for 小数点之前的那部分
        if residual == 0: # 如果是整数直接返回
            return res
        res += "."
        res_decimal = '' #res_decimal account for 小数点之后的那部分
        dic = {residual:0} #dic 用来记录余数还有这个余数对应的在res_decimal 这部分的位数
        i = 1
        while True:
            numerator = residual*10
            val = numerator // denominator
            residual = numerator % denominator
            # 以下这三种情况都要将str（val）加进去
            if residual == 0:
                return res + res_decimal + str(val)  # 返回小数点之前的加上小数点之后的加上当前的那一位
            if residual not in dic:
                dic[residual] = i
                res_decimal += str(val)
                i+=1
            else:
                ind = dic[residual]
                res_decimal += str(val) # 不要忘记加上这个值
                return res + res_decimal[:ind] + "("+res_decimal[ind:]+')' #注意res_decimal[:ind] 不包含ind这个点

x = Solution()
print(x.fractionToDecimal(numerator=1, denominator=6))
# 这道题主要是hashtable 的利用，主要逻辑是用hashtable 记录数字相除之后的余数 如果这个余数出现过， 那么说明小数开始循环。
# 这个问题细节比较多 略麻烦
