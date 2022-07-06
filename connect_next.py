from typing import List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        result = f"Node({self.val}"
        if self.left:
            result += f", left={self.left}"
        if self.right:
            result += f", right={self.right}"
        if self.next:
            result += f", next={self.next}"
        result += ")"

        return result


from collections import defaultdict
from itertools import pairwise
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        depth_map = defaultdict(list)
        stack = [(root, 0)]
        max_depth = 0
        while stack:
            current, depth = stack.pop()
            depth_map[depth].append(current)
            max_depth = max(max_depth, depth)
            if current.right:
                stack.append((current.right, depth + 1))
            if current.left:
                stack.append((current.left, depth + 1))

        for depth in range(max_depth + 1):
            for lhs, rhs in pairwise(depth_map[depth]):
                lhs.next = rhs
        return root





if __name__ == "__main__":
    s = Solution()
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    result = s.connect(root)
    print(s.connect(root))
