from typing import List, Optional

class ListNodeIter:

    def __init__(self, node):
        self.node = node

    def __next__(self):
        if self.node:
            val = self.node.val
            self.node = self.node.next
            return val
        raise StopIteration

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        return ListNodeIter(self)

    def __repr__(self):
        return f"ListNode({self.val}, next={self.next})"


def make_listNode(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    return ListNode(lst[0], next=make_listNode(lst[1:]))

def listNodeLen(head: Optional[ListNode]) -> int:
    length = 0
    current = head
    while current:
        current = current.next
        length += 1
    return length

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 0 or head is None or head.next is None:
            return head

        length = listNodeLen(head)
        k = k % length

        if k == 0:
            return head

        k_from_behind = length - k

        i = k_from_behind
        kthElement = head
        prev = None
        while i > 0:
            prev = kthElement
            kthElement = kthElement.next
            i -= 1
        prev.next = None

        current = kthElement
        while current.next:
            current = current.next
        current.next = head

        return kthElement

if __name__ == "__main__":
    listNode = make_listNode([1, 2])
    s = Solution()
    print(s.rotateRight(listNode, 2))
