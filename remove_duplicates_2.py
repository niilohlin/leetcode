from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tracker = 0
        for i in range(len(nums)):
            if nums[tracker] == nums[i]:
                continue
            tracker += 1
            nums[tracker] = nums[i]

        return tracker + 1


if __name__ == "__main__":
    s = Solution()
    a = [0,0,1,1,1,2,2,3,3,4]
    k = s.removeDuplicates(a)
    print(k)
    print(a[:k])
    print(a)
