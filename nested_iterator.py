# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import Iterator, List

class NestedInteger:
    def __init__(self, lst):
        self.lst = lst
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

        return type(self.lst) == int


    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.lst

    def getList(self) -> List['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.lst


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [iter(nestedList)]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            current = self.stack.pop()
            value = next(current, None)
            if value:
                self.stack.append(current)

                if value.isInteger():
                    self.stack.append(value)
                    return True
                else:
                    self.stack.append(iter(value.getList()))
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    nested_list = [NestedInteger([NestedInteger([NestedInteger(5)]), NestedInteger(3)])]

    i = NestedIterator(nested_list)
    while i.hasNext():
        print( i.next() )
