from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 and list2 is None:
            return list1
        if list2 and list1 is None:
            return list2

        if list1.val < list2.val:
            next = list1.next
            list1.next = self.mergeTwoLists(next, list2)
            return list1
        next = list2.next
        list2.next = self.mergeTwoLists(list1, next)
        return list2





if __name__ == "__main__":
    s = Solution()
    print(s.solution())
