#/usr/bin/env python

from typing import List

class Pool:
    def __init__(self, lst):
        self.max = max(lst)
        self.min = min(lst)
        self.lst = lst

    def split_on(self, level):
        result = []
        sublist = []
        for element in self.lst:
            if element < level:
                if len(sublist) > 0:
                    result.append(Pool(sublist))
                sublist = []
                continue
            sublist.append(element)
        if len(sublist) > 0:
            result.append(Pool(sublist))

        return list(filter(lambda l: len(l.lst) != 0, result))


class Solution:

    def naive_solution(self, heights: Pool, level=1) -> int:
        if level > heights.max:
            return 0
        if level <= heights.min:
            return max(len(heights.lst) * level, self.naive_solution(heights, max(level + 1, heights.min)))

        splitted = heights.split_on(level)
        return max(map(lambda sub_heights: self.naive_solution(sub_heights, level), splitted))

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.naive_solution(Pool(heights))

if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([2,1,2]) == 3
    pass

