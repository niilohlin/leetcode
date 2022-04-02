from typing import List


def splits(nums: List[int], indexes: List[int]) -> List[List[int]]:
    def splits_iterator():
        all_indexes = ([0] + indexes + [len(nums)])
        for start, end in zip(all_indexes, all_indexes[1:]):
            yield nums[start:end]
    return list(splits_iterator())


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        split_indexes = list(range(m - 1))
        all_lists = splits(nums, split_indexes)




if __name__ == "__main__":
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
