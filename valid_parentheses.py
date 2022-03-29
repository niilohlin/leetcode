from typing import List


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c in "{([":
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            if c == ']' and stack[-1] == '[':
                stack.pop()
                continue
            if c == ')' and stack[-1] == '(':
                stack.pop()
                continue
            if c == '}' and stack[-1] == '{':
                stack.pop()
                continue
            return False
        return len(stack) == 0

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
