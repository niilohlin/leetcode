from typing import List

from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)

        longest = 0
        for num in nums:
            if not num - 1 in n_set:
                n = num
                while n in n_set:
                    n += 1
                longest = max(longest, n - num)

        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
