from typing import List

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        result = 0
        counter = Counter(nums)
        if k == 0:
            for key, value in counter.items():
                if value > 1:
                    result += 1
            return result

        for key, value in counter.items():
            if key + k in counter:
                result += 1
        return result





if __name__ == "__main__":
    s = Solution()
    print(s.findPairs([3,1,4,1,5], 2))
