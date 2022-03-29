from typing import List

from enum import Flag
from math import log2
from itertools import combinations_with_replacement

class Tile(Flag):
    NONE = 0
    ONE = 1
    TWO = 1 << 1
    THREE = 1 << 2
    FOUR = 1 << 3
    FIVE = 1 << 4
    SIX = 1 << 5
    SEVEN = 1 << 6
    EIGHT = 1 << 7
    NINE = 1 << 8

    def __len__(self):
        result = 0
        for i in range(9):
            if self.value & (1 << i):
                result += 1
        return result



def transpose(board):
    return list(map(list, zip(*board)))

def is_unique(lst):
    values = list(filter(lambda x: x != ".", lst))
    return len(values) == len(set(values))

def all_map(f, it):
    return all(map(f, it))


def box(x, y, board):
    for i in range(3):
        for j in range(3):
            yield board[x * 3 + i][y * 3 + j]

def unbox(x, y, _box, board):
    result_board = [[val for val in row] for row in board]
    for i in range(3):
        for j in range(3):
            result_board[x * 3 + i][y * 3 + j] = _box[i * 3 + j]
    return result_board


def to_board(bit_board):
    board = [["." for _ in range(9)] for _ in range(9)]
    for x, row in enumerate(board):
        for y, _ in enumerate(row):
            for tile in Tile:
                if bit_board[x][y] == tile:
                    board[x][y] = str(int(log2(tile.value)) + 1)
                    break

    return board

def to_bit_board(board):
    bit_board = [[0 for _ in range(9)] for _ in range(9)]

    for x, row in enumerate(board):
        for y, val in enumerate(row):

            if val == ".":
                bit_board[x][y] = ~Tile.NONE
            else:
                bit_board[x][y] = list(Tile)[int(val)]
    return bit_board


def decided_value(bit):
    for tile in list(Tile)[1:]:
        if bit == tile:
            return tile
    return None

def filter_unique(bit_row):
    decided_tiles = Tile.NONE
    row = list(bit_row)
    for value in row:
        if len(value) == 1:
            decided_tiles |= value

    result = []
    for tile in row:
        if len(tile) == 1:
            result.append(tile)
        else:
            result.append(tile & ~decided_tiles)
    return result #[tile & ~decided_tiles for tile in bit_row]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not all_map(is_unique, board):
            return False

        if not all_map(is_unique, transpose(board)):
            return False

        if not all_map(is_unique, [box(x, y, board) for x in range(3) for y in range(3)]):
            return False

        return True


    def solveSudoku(self, board: List[List[str]]) -> None:

        while True:
            bit_board = to_bit_board(board)
            filtered_rows = [filter_unique(row) for row in bit_board]
            filtered_columns = transpose([filter_unique(col) for col in transpose(filtered_rows)])
            filtered_boxes = [(x, y, filter_unique(box(x, y, filtered_columns))) for x in range(3) for y in range(3)]
            unboxed_board = [[Tile.NONE for _ in range(9)] for _ in range(9)]
            for (x, y, filtered_box) in filtered_boxes:
                unboxed_board = unbox(x, y, filtered_box, unboxed_board)

            next_board = to_board(unboxed_board)
            if str(board) == str(next_board):
                break
            for x in range(9):
                for y in range(9):
                    board[x][y] = next_board[x][y]

def print_board(board):
    for row in board:
        print(row)
if __name__ == "__main__":
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.solveSudoku(board))
