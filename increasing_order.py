from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leftNodes(self, node):
        if node is None:
            return

        self.stack.append(node)
        while node.left:
            self.stack.append(node.left)
            node = node.left

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.stack = []
        self.leftNodes(root)
        new_root = self.stack.pop()
        self.leftNodes(new_root.right)
        current = new_root
        while self.stack:
            current.left = None
            current.right = self.stack.pop()
            self.leftNodes(current.right.right)
            current = current.right
        current.right = None
        current.left = None

        return new_root



if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(
        val=5,
        left=TreeNode(
            val=3,
            left=TreeNode(val=2,left=TreeNode(val=1)),
            right=TreeNode(val=4)
        ),
        right=TreeNode(
            val=6,
            right=TreeNode(
                val=8,
                left=TreeNode(val=7),
                right=TreeNode(val=9)
            )
        )
    )

    other = TreeNode(
        val=2,
        left=TreeNode(val=1),
        right=TreeNode(val=4, left=TreeNode(val=3))
    )

    newTree = (s.increasingBST(other))
    print("tree")
