from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water_area = 0
        start = 0
        end = len(height) - 1
        indexed_heights = list(enumerate(height))

        while start != end:
            area = min(indexed_heights[start][1], indexed_heights[end][1]) * (indexed_heights[end][0] - indexed_heights[start][0])
            max_water_area = max(max_water_area, area)

            indexed_heights = list(filter[])
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_water_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
