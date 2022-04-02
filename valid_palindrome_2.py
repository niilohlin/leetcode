from typing import List

def validPalindrome(s):
    return s == "".join(reversed(s))

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if validPalindrome(s):
            return True

        for i in range(len(s) // 2):
            inverse = len(s) - 1 - i
            if s[i] != s[inverse]:
                return validPalindrome(s[:i] + s[i+1:]) or validPalindrome(s[:inverse] + s[inverse+1:])
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("cbbcc"))
