from typing import List, Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def fixedpoint(f, start, stop):
    while start != stop:
        yield start
        start = f(start)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        indexes = {}
        current = head
        i = 0
        while current:
            indexes[current] = i
            i += 1
            current = current.next

        result = []
        current = head
        while current:
            if current.next:
                result.append((current.val, indexes[current.next]))
            else:
                result.append((current.val, None))
            current = current.next

        new_head = Node(result[0][0])
        current = new_head

        for i in result[1:]:
            current.next = Node(i[0])
            current = current.next

        new_head_list =
        current = new_head
        for i in result:
            current.random =





def make_listNode(lst: List[int]) -> Optional[Node]:
    if not lst:
        return None
    return Node(lst[0], next=make_listNode(lst[1:]))

if __name__ == "__main__":
    s = Solution()
    lst = make_listNode([1, 2, 3, 4])
    print(s.copyRandomList())
