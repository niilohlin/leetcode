from typing import List


def insert_between(x, lst):
    for i in range(len(lst)):
        yield lst[:i] + [x] + lst[i:]
    yield lst + [x]

def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    head = nums[0]
    tail = nums[1:]
    return [y for x in permute(tail) for y in insert_between(head, x)]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(permute(sorted(nums)))

if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 3]))
