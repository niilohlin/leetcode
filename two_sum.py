from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i in range(len(nums)):
            if target - nums[i] in nums_set:
                index = nums.index(target - nums[i])
                if index != i:
                    return [i, index]
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))