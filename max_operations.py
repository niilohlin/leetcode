from typing import List

from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        counter = Counter(nums)
        while True:
            for n in counter.keys():
                if counter[n] == 0:
                    continue
                c = k - n
                if counter[c] >= [c, n].count(c):
                    counter[c] -= 1
                    counter[n] -= 1
                    result += 1
                    break
            else:
                return result



if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([2,2,2,3,1,1,4,1], 4))
