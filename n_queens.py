from typing import List


def check_queens(board):
    queen_poss = set()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != "Q":
                continue
            for q_pos in queen_poss:
                if int(q_pos.real) == x:
                    return False
                if int(q_pos.imag) == y:
                    return False
                for dir in [(1 + 1j), (1 - 1j), (-1 + 1j), (-1 - 1j)]:
                    for z in range(1, len(board)):
                        if q_pos + dir * z == complex(x, y):
                            return False
            queen_poss.add(complex(x, y))
    return True


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n] * n
        stack = [board]
        for i in range(n):
            candidates = stack.copy()
            stack = []
            for board in candidates:
                for x in range(len(board)):
                    for y in range(len(board[x])):
                        if board[x][y] != "Q":
                            board[x][y] = "Q"
                            if check_queens(board):
                                stack.append(board)
        return stack


def to_board(n):
    def n_to_board(s):
        res = []
        for x in range(n):
            row = ""
            for y in range(n):
                if complex(x, y) in s:
                    row += "Q"
                else:
                    row += "."
            res.append(row)
        return res
    return n_to_board

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = set()
        stack = [board]
        result = set()
        while stack:
            board = stack.pop()
            for x in range(n):
                for y in range(n):
                    for q_pos in board:
                        if int(q_pos.real) == x:
                            break
                        if int(q_pos.imag) == y:
                            break
                        def is_diag():
                            for dir in [(1 + 1j), (1 - 1j), (-1 + 1j), (-1 - 1j)]:
                                for z in range(1, n):
                                    if q_pos + dir * z == complex(x, y):
                                        return True
                            return False
                        if is_diag():
                            break
                    else:
                        new_candidate = board.copy()
                        new_candidate.add(complex(x, y))
                        stack.append(new_candidate)

            if len(board) == n:
                result.add(tuple(sorted(board, key=lambda c: (c.real, c.imag))))
        return list(map(to_board(n), result))

def print_board(board):
    for row in board:
        print(row)

if __name__ == "__main__":
    s = Solution()
    for res in s.solveNQueens(4):
        print_board(to_board(res, 4))
        print("")
