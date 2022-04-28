from typing import List


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_element = None
        if self.iterator.hasNext():
            self.next_element = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_element

    def next(self):
        """
        :rtype: int
        """
        result = self.next_element
        self.next_element = None
        if self.iterator.hasNext():
            self.next_element = self.iterator.next()
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.next_element)



if __name__ == "__main__":
    s = Solution()
    print(s.solution())
