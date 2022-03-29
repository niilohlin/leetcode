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



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next.next
            # result.next = node
            node = node.next
        return head



if __name__ == "__main__":
    listNode = make_listNode([1, 2, 3, 3, 4])
    s = Solution()
    new_listNode = s.deleteDuplicates(listNode)
