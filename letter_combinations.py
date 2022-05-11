from typing import List

digit_map = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]

from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return list(map(lambda pair: ''.join(pair), product(*map(lambda d: digit_map[ord(d) - 50], digits))))




if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations(""))
