#问题的关键是在当前的class不能access nums， 那么需要temparay varaible
#另外一点是一般peek只被call一次。不会有多次情况。那么我们其实不需要list 只需要variable

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.cache:
            if not self.iterator.hasNext():
                return None
            else:
                x = self.iterator.next()
                self.cache = x
                return x
        else:
            return self.cache

    def next(self):
        """
        :rtype: int
        """
        if not self.cache:
            return self.iterator.next()
        else:
            tmp = self.cache
            self.cache = None
            return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext() or self.cache is not None

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
