from typing import List

from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum12 = defaultdict(int)

        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)
        nums4_set = set(nums4)

        for i in nums1_set:
            for j in nums2_set:
                sum12[i + j] += nums1.count(i) * nums2.count(j)

        sum34 = defaultdict(int)
        for i in nums3_set:
            for j in nums4_set:
                sum34[i + j] += nums3.count(i) * nums4.count(j)

        tuples = 0
        for s, times in sum12.items():
            tuples += sum34[-s] * times

        return tuples


if __name__ == "__main__":
    s = Solution()
    print(s.fourSumCount([0,1,-1], [-1,1,0], [0,0,1], [-1,1,1]))
