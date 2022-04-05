from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        k_from_behind = length - k

        index = 1
        from_ahead = None
        from_behind = None
        current = head
        while current:
            if index == k:
                from_ahead = current
            elif index == k_from_behind:
                from_behind = current
            current = current.next
            index += 1
        



if __name__ == "__main__":
    s = Solution()
    print(s.solution())
