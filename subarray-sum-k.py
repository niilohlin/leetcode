from typing import List


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = 0
        sum = 0
        d = defaultdict(int)
        d[0] = 1

        for n in nums:
            sum += n
            result += d.get(sum-k, 0)
            d[sum] += 1


        return result




if __name__ == "__main__":
    s = Solution()
    # assert (s.subarraySum([1, 1, 1], 2) == 2)
    assert (s.subarraySum([1, 2, 0, 3], 3) == 2)
    assert (s.subarraySum([1, 1, 1, 0], 2) == 3)
