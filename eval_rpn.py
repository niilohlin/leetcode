from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_map = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }
        tokens.reverse()
        while tokens:
            current = tokens.pop()
            operator = op_map.get(current)
            if operator:
                lhs = stack.pop()
                rhs = stack.pop()
                stack.append(operator(rhs, lhs))
            else:
                stack.append(int(current))

        return stack[0]

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
