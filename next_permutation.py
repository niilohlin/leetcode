from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in reversed(range(len(nums))):
            for j in reversed(range(i)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

                    for i in range(j + 1, len(nums[j+1:]) // 2):
                        nums[i], nums[-i - 1] = nums[-i - 1], nums[i]
                    return

        for i in range(len(nums) // 2):
            nums[i], nums[-i - 1] = nums[-i - 1], nums[i]

if __name__ == "__main__":
    s = Solution()
    l = [1,3,2]
    s.nextPermutation(l)
    print("expected: " + str([2,1,3]))
    print(l)
