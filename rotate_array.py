from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        backup = nums.copy()
        l = len(nums)
        for i in range(len(nums)):
            nums[i] = backup[(i - k) % l]

def test(input, k, expected):
    s = Solution()
    s.rotate(input, k)
    assert tuple(input) == tuple(expected)


if __name__ == "__main__":
    test([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4])
    test([-1], 2, [-1])
    test([1, 2], 3, [2, 1])
