from typing import List

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s) - k + 1):
            print(s[i:i+k])
            codes.add(s[i:i+k])
        return 2 ** k == len(codes)

if __name__ == "__main__":
    s = Solution()
    print(s.hasAllCodes("00110110", 2))

