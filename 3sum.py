from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        num_indexes = dict()

        for i, n in enumerate(nums):
            num_indexes[n] = i

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if num_indexes.get(-(nums[i] + nums[j]), -1) >= j + 1:
                    result.append(sorted([nums[i], nums[j], -(nums[i] + nums[j])]))
        return list(map(list, set(map(tuple, result))))




if __name__ == "__main__":
    s = Solution()

    print(s.threeSum([-1,0,1,2,-1,-4]))
