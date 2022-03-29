# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], overflow = 0) -> Optional[ListNode]:
        if l1 == None and l2 == None and overflow == 0:
            return None
        if l1 == None and l2 == None and overflow:
            return ListNode(overflow)
        if l1 == None:
            return ListNode((l2.val + overflow) % 10, next=self.addTwoNumbers(l1, l2.next, (l2.val + overflow) // 10))
        if l2 == None:
            return ListNode((l1.val + overflow) % 10, next=self.addTwoNumbers(l1.next, l2, (l1.val + overflow) // 10))

        return ListNode((l1.val + l2.val + overflow) % 10, next=self.addTwoNumbers(l1.next, l2.next, (l1.val + l2.val + overflow) // 10))


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([2, 1, 2]) == 3
    pass
