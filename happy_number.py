class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """

    def isHappy(self, n):
        # write your code here
        square_sum = self.digit_manipulation(n)
        record = [square_sum]
        while True:
            if square_sum == 1:
                return True
            else:
                new_square_sum = self.digit_manipulation(square_sum)
                if new_square_sum in record:
                    return False
                else:
                    record.append(new_square_sum)
                    square_sum = new_square_sum

    def digit_manipulation(self, number):
        digits = []
        temp = number
        while temp > 0:
            remainder = temp % 10
            digits.append(remainder)
            temp = temp // 10

        return sum([x ** 2 for x in digits])


x = Solution()
print(x.isHappy(5))

# by definition, no brainer,