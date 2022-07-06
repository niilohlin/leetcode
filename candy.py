from typing import List


from itertools import pairwise

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1
        candies = 0
        curr_candies = 1
        for i, t in enumerate(pairwise(ratings)):
            x, x1 = t
            if x < x1:
                candies +=
            elif x > x1:
                slopes.append(-1)
            else:
                slopes.append(0)




if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 2, 2]))
