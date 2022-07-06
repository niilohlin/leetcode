from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        out = m + n - 1
        m -= 1
        n -= 1
        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[out] = nums1[m]
                m -= 1
            else:
                nums1[out] = nums2[n]
                n -= 1
            out -= 1






if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    print(s.merge(a, 3, b, 3))
    print(a)
