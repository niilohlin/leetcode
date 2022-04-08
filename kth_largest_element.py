from typing import List
import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(sorted(nums))

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]

