from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid[0])
        n = len(grid)
        real_k = (-k) % (n * m)

        flattened = [cell for row in grid for cell in row]

        return [[flattened[(j * m + i + real_k) % len(flattened)] for i in range(m)] for j in range(n)]

if __name__ == "__main__":
    s = Solution()
    print(s.shiftGrid([[1, 2, 3], [4, 5, 6]], 1))
