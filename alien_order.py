from typing import List

class NodeIter:
    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration()
        val = self.node.val
        self.node = self.node.next
        return val

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        if prev:
            prev.next = self
        self.next = next
        if next:
            next.prev = self

    def insert_right(self, val):
        Node(val, prev=self, next=self.next)

    def insert_left(self, val):
        Node(val, prev=self.prev, next=self)

    def insert_ordered(self, lhs, rhs):
        c = self
        while c.next:
            if c.val == lhs:
                if c.next and c.next.val == rhs:
                    return
                c.insert_right(rhs)
                return
            if c.val == rhs:
                if c.prev and c.prev.val == lhs:
                    return
                c.insert_left(lhs)
                return
            c = c.next
        self.insert_right(rhs)
        self.insert_right(lhs)

    def __iter__(self):
        c = self
        while c.prev:
            c = c.prev
        return NodeIter(c)


class Solution:
    def alien_order(self, words: List[str]) -> str:
        __node_head = object()
        ordering = Node(__node_head)

        for lhs, rhs in zip(words, words[1:]):
            for c1, c2 in zip(lhs, rhs):
                if c1 == c2:
                    continue
                ordering.insert_ordered(c1, c2)
                break

        all_letters = list(sorted({ c for word in words for c in word }))

        existing_letters = set(ordering)

        # missing_alphabet = list(sorted(all_letters.difference(existing_letters)))

        for c1, c2 in zip(all_letters, all_letters[1:]):
            if c1 in existing_letters and c2 in existing_letters:
                continue
            ordering.insert_ordered(c1, c2)

        return "".join(list(ordering)[1:])

if __name__ == "__main__":
    s = Solution()
    print(s.alien_order(["zy","zx"]))
    print(s.alien_order(["wrt","wrf","er","ett","rftt"]))
