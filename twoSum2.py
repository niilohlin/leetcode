from typing import List

import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hi = len(numbers) - 1
        lo = 0

        while True:
            if numbers[hi] + numbers[lo] == target:
                return [lo + 1, hi + 1]
            hi = bisect.bisect_left(numbers, target, lo=lo, hi=hi)
            lo = bisect.bisect(numbers, target - numbers[hi], lo=lo, hi=hi)

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
