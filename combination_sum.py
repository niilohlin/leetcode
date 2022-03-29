from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.calHelper([], 0, candidates, target, res)
        return res

    def calHelper(self, currentList, startIdx, candidates, target, res):
        if target == 0:
            res.append(currentList)
            return

        for i in range(startIdx, len(candidates)):
            num = candidates[i]
            if num <= target:
                self.calHelper(currentList + [num], i, candidates, target - num, res)
            else:
                break


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
