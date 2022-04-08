from typing import List

from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counted = Counter(arr)

        items = list(counted.items())
        result = 0
        for i in range(len(items)):
            for j in range(i, len(items)):
                if target - (items[i][0] + items[j][0]) in counted:
                    print(f"{(items[i][0], items[j][0], target - (items[i][0] + items[j][0]) )}")

        return result




if __name__ == "__main__":
    s = Solution()
    print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
