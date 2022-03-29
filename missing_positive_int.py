
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen_nums = set(filter(lambda x: x > 0, nums))

        i = 1
        while i in seen_nums:
            i += 1

        return i

if __name__ == "__main__":
    s = Solution()
    assert(s.firstMissingPositive([1,2,0]) == 3)
    assert(s.firstMissingPositive([3, 4, -1, 1]) == 2)
    assert(s.firstMissingPositive([7,8,9,11,12]) == 1)
