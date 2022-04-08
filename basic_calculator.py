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

# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def rpn_stack(stack: List[Union[str, int]]) -> List[Union[str, int]]:
    """
    Turn lexed stack into rpn, e.g
    [2, '-', 11, '+', 2] -> [2, 11, '-' 2, '+']
    """
    stack = list(reversed(stack))
    operator_stack = []
    result_stack = []


    while stack:
        current = stack.pop()
        if type(current) == int:
            result_stack.append(current)
        elif current == '-':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                result_stack.append(operator_stack.pop())
            if len(result_stack) == 0 or len(operator_stack) > 0 and operator_stack[-1] == '(':
                operator_stack.append('n')
            else:
                operator_stack.append(current)
        elif current in '+':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                result_stack.append(operator_stack.pop())
            operator_stack.append(current)
        elif current == '(':
            operator_stack.append(current)
        elif current == ')':
            assert len(operator_stack) != 0
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                assert len(operator_stack) != 0
                result_stack.append(operator_stack.pop())
            assert operator_stack[-1] == '('
            operator_stack.pop()
            if len(operator_stack) > 0 and operator_stack[-1] in '+-':
                result_stack.append(operator_stack.pop())

    while operator_stack:
        assert operator_stack[-1] != '('
        result_stack.append(operator_stack.pop())

    return result_stack

def eval_stack(stack: List[Union[str, int]]) -> int:
    """
    evaluates an rpn stack
    [2, 11, '-' 2, '+'] -> -11
    """
    i = 0
    while i < len(stack):
        if stack[i] == '+':
            stack = stack[:i - 2] + [stack[i - 2] + stack[i - 1]] + stack[i + 1:]
            i = 0
        elif stack[i] == '-':
            stack = stack[:i - 2] + [stack[i - 2] - stack[i - 1]] + stack[i + 1:]
            i = 0
        elif stack[i] == 'n':
            stack[i - 1] *= -1
            stack = stack[:i] + stack[i + 1:]
            i = 0
        else:
            i += 1

    return stack[0]


class Solution:
    def calculate(self, s: str) -> int:

        stack = list(lex(s))
        operator_stack = rpn_stack(stack)
        value = eval_stack(operator_stack)
        return value

if __name__ == "__main__":
    s = Solution()
    # print(s.calculate("-2"))
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
