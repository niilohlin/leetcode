from typing import List

from collections import Counter
from itertools import groupby


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        counted = sorted(map(lambda s: (tuple(sorted(Counter(s).items())), s), strs))
        for key, it in groupby(counted, lambda x: x[0]):
            result.append(list(map(lambda t: t[1], it)))
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
