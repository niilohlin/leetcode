from typing import List

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lo = 0
        hi = len(s) - 1
        count = Counter(s)
        t_count = Counter(t)



if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
