# 这道题是偏向应用的一道题目， 比较实用，在实际种也可以用到
import time
class Foo(object):
    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done = True

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.first_done:
            time.sleep(0.0001) # 也可以用pass 但是时间会增长。

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done = True

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.second_done:
            time.sleep(0.0001)

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
