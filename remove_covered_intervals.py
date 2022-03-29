from typing import List


import bisect
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = list(map(tuple, intervals))
        intervals.sort()

        longest_start, longest_end = 0, 0
        for start, end in intervals:
            if end - start >= longest_end - longest_start:
                longest_start, longest_end = start, end

        index = bisect.bisect_left(intervals, (longest_start, longest_end))
        intervals.pop(index)
        removing = []
        for start, end in intervals[index:]:
            if start >= longest_end:
                break
            if end <= longest_end:
                result.append((start, end))
        return







if __name__ == "__main__":
    s = Solution()
    print(s.removeCoveredIntervals([[1,4],[3,6],[2,8]]))

