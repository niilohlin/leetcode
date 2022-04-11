from typing import List, Union

def lex(s: str) -> List[Union[str, int]]:
    """
    Lex string into tokens. e.g.
    ' 2-11 + 2   ' -> [2, '-', 11, '+', 2]

    """
    i = 0
    while i < len(s):
        if s[i] == " ":
            i += 1
            continue
        if s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            yield int(s[i:j])
            i = j
            continue
        yield s[i]
        i += 1

class Solution:
    def calculate(self, s: str) -> int:
        stack = list(lex(s))
        result = 0

        i = 0
        while i + 2 < len(stack):

            if type(stack[i]) == int and stack[i + 1] == '-' and type(stack[i + 2]) == int:
                stack = stack[:i] + [stack[i] - stack[i + 2]] + stack[i + 3:]
                i = 0
                continue
            if type(stack[i]) == int and stack[i + 1] == '+' and type(stack[i + 2]) == int:
                stack = stack[:i] + [stack[i] + stack[i + 2]] + stack[i + 3:]
                i = 0
                continue
            if stack[i] == '(' and type(stack[i + 1]) == int and stack[i + 2] == ')':
                stack = stack[:i] + [stack[i] + stack[i + 2]] + stack[i + 3:]
                i = 0
                continue
            i += 1


        print("stack: " + str(stack))
        return stack[0]
if __name__ == "__main__":
    s = Solution()
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
