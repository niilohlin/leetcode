
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        max_profit = 0
        start = 0
        end = 1
        while end < len(prices):
            if prices[start] < prices[end]:
                max_profit = max(max_profit, prices[end] - prices[start])
            else:
                start = end
            end += 1
        return max_profit




if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 4, 2]))
