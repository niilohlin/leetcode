from typing import List, Optional


# Definition for singly-linked list.
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


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        node, node_nxt = head, head.next
        while node and node_nxt:
            node.val, node_nxt.val = node_nxt.val, node.val
            node = node_nxt.next
            if node: node_nxt = node.next
        return head


def make_listNode(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    return ListNode(lst[0], next=make_listNode(lst[1:]))


if __name__ == "__main__":
    listNode = make_listNode([1, 2, 3, 4])
    s = Solution()
    new_listNode = s.swapPairs(listNode)

    print(new_listNode)
