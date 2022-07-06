from typing import List

from collections import defaultdict

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        tiles = {complex(x, y): matrix[x][y] for x in range(len(matrix)) for y in range(len(matrix[0]))}
        paths = defaultdict(lambda: 1)
        for (pos, val) in sorted(tiles.items(), key=lambda x: x[1]):
            for diff in [(-1 + 0j), (1 + 0j), (1j), (-1j)]:
                neighbour = pos + diff

                if neighbour in tiles and tiles[neighbour] > tiles[pos]:
                    paths[neighbour] = max(paths[neighbour], paths[pos] + 1)

        if paths:
            return paths[max(paths.items(), key=lambda x: x[1])[0]]
        return len(matrix)


if __name__ == "__main__":
    s = Solution()

    matrix = [[3, 4, 5],
              [3, 2, 6],
              [2, 2, 1]]
    print(s.longestIncreasingPath(matrix))
