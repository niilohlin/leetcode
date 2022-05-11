from typing import List
from bisect import insort, bisect_left


class MinStack:
    def __init__(self):
        self.stack = []
        self.sorted_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        insort(self.sorted_list, val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.sorted_list.pop(bisect_left(self.sorted_list, val))

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_list[0]


if __name__ == "__main__":
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)
    a.getMin()
    a.pop()
    a.top()
    a.getMin()
