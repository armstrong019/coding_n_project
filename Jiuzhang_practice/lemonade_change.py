# rule based， 比较直接的一道题目。
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True
        if bills[0] != 5:
            return False
        dic = {5: 0, 10: 0, 20: 0}
        for i in range(len(bills)):
            if bills[i] == 5:
                dic[5] += 1
            else:
                if bills[i] == 10:
                    if dic[5] == 0:
                        return False
                    else:
                        dic[5] -= 1
                        dic[10] += 1
                else:  # bills[i]==20:
                    if dic[10] >= 1 and dic[5] >= 1: # 尽可能把10元的钱先找回去
                        dic[10] -= 1
                        dic[5] -= 1
                        dic[20] += 1
                    elif dic[10] == 0 and dic[5] >= 3:
                        dic[5] -= 3
                        dic[20] += 1
                    else:
                        return False
        return True
