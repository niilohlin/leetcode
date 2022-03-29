from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = hare = nums[0]

        while True:
            hare = nums[nums[hare]]
            turtle = nums[turtle]
            if turtle == hare:
                break

        turtle = nums[0]
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]

        return turtle

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1,3,4,2,1]))
