from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        return BSTIterator(self)

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        self._add_left_nodes(root)

    def _add_left_nodes(self, node):
        if not node:
            return

        self.stack.append(node)

        while node.left:
            self.stack.append(node.left)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._add_left_nodes(node.right)
        return node.val

    def hasNext(self) -> bool:
        return self.stack


if __name__ == "__main__":
    tree = TreeNode(val=3,left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(val=2)))

    iterator = BSTIterator(tree)
    assert iterator.next() == 1
    v = iterator.next()
    assert v == 3
    # [1, 3, 2, 4]
    print(list(tree))
