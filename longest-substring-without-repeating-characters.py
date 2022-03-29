
def is_unique(str):
    return len(set(str)) == len(str)


# indexes = {}
# for i, c in enumerate(s):
#     indexes[c] = indexes.get(c, []) + [i]


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        end = 0
        max_length = 0
        last_seen = {}
        while end < len(s):
            if s[end] in last_seen:
                start += 1
                end += 1
            else:
                last_seen[s[end]] = end
                end += 1
                max_length = max(max_length, end - start)

        return max_length




if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("pwwkew"))