from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_array(self):
        if self.next:
            return [self.val] + self.next.to_array()
        return [self.val]


    def __repr__(self):
        return "ListNode(" + str(self.to_array()) + ")"



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        times = length // k

        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head


#### Test code

def make_listNode(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    return ListNode(lst[0], next=make_listNode(lst[1:]))


listNode = make_listNode([1, 2, 3, 4, 5])

s = Solution()
print(s.reverseKGroup(listNode, 2))
