from typing import List


from collections import Counter
class Solution:
    def trap(self, height: List[int]) -> int:
        highest = 0
        result = 0
        accumulator = 0

        for h in height:
            if h >= highest:
                result += accumulator
                accumulator = 0
                highest = h
            else:
                accumulator += highest - h
        highest = 0
        accumulator = 0

        for h in reversed(height):
            if h > highest:
                result += accumulator
                accumulator = 0
                highest = h
            else:
                accumulator += highest - h
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 1, 0]))
