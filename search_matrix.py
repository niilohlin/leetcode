from typing import List, Sequence
import bisect

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)

    def __len__(self):
        return self.width * self.height

    def __getitem__(self, item):
        (row, col) = divmod(item, self.width)
        return self.matrix[row][col]


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = Matrix(matrix)
        index = bisect.bisect_left(m, target)
        return index < len(m) and m[index] == target

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1, 1]], 0))
