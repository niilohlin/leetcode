from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for c in s:
            if c == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(c)

        t_stack = []
        for c in t:
            if c == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(c)
        return s_stack == t_stack

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
