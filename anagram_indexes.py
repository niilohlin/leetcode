from typing import List

def dict_equal(d1, d2):
    for k, v in d1.items():
        if d2.get(k, 0) != v:
            return False
    for k, v in d2.items():
        if d1.get(k, 0) != v:
            return False
    return True

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        anagram_dict = {}
        for c in p:
            anagram_dict[c] = anagram_dict.get(c, 0) + 1

        start = 0
        end = len(p)

        current_dict = {}
        for i in range(len(p)):
            current_dict[s[i]] = current_dict.get(s[i], 0) + 1

        result = []
        while end <= len(s):
            if dict_equal(anagram_dict, current_dict):
                result.append(start)

            if end == len(s):
                break

            current_dict[s[end]] = current_dict.get(s[end], 0) + 1
            current_dict[s[start]] = current_dict.get(s[start], 0) - 1
            end += 1
            start += 1

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("abab", "ab"))
