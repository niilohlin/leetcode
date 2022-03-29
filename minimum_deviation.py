from typing import List
from bisect import insort

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] *= 2

        nums.sort()
        result = 10 ** 9
        while True:
            largest = nums[-1]
            if largest % 2 == 0:
                largest = nums.pop() // 2
                insort(nums, largest)
                result = min(result, nums[-1] - nums[0])
            else:
                break
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minimumDeviation([3,5]))
