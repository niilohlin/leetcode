from typing import List

import bisect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = list(sorted(nums[:k]))
        for n in nums[k:]:
            if n >= queue[-1]:
                bisect.insort(queue, n)
                queue.pop()
        return queue[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
