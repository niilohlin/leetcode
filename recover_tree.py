from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = [(None, root, None)]

        while stack:
            less, current, more = stack.pop()
            if current.val





if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(val=3,left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(val=2)))
    print(s.recoverTree(tree))
