from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        acc = 1
        for i in range(len(nums)):
            acc *= nums[i]
            prefixes[i] = acc

        acc = 1
        for i in reversed(range(len(nums))):
            acc *= nums[i]
            suffixes[i] = acc

        suffixes.append(1)
        prefixes.append(1)

        result = []
        for i in range(len(nums)):
            result.append(prefixes[i - 1] * suffixes[i + 1])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
