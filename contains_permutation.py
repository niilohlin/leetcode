from typing import List


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counter = Counter(s1)

        rolling_counter = Counter(s2[:len(s1)])
        if rolling_counter == counter:
            return True

        for i in range(len(s1), len(s2)):
            rolling_counter.subtract(s2[i - len(s1)])
            rolling_counter.update(s2[i])
            if rolling_counter == counter:
                return True
        return False



if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("hello", "ooolleoooleh"))
