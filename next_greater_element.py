from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack[-1]] = num
                stack.pop()
            stack.append(num)

        return [mapping.get(n, -1) for n in nums1]




if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [5,4,3,2,1, 2, 3, 4, 5]))
