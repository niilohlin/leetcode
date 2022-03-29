from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        tracker = 2
        for i in range(2, len(nums)):
            if nums[tracker - 2] != nums[i]:
                nums[tracker] = nums[i]
                tracker += 1

        return tracker


if __name__ == "__main__":
    s = Solution()
    a = [1,1,1,2,2,3]
    print(s.removeDuplicates(a))
    print(a)
