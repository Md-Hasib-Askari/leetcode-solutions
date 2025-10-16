from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # leftDepth = self.maxDepth(root.left)
        # rightDepth = self.maxDepth(root.right)

        # return 1 + max(leftDepth, rightDepth)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    solution = Solution()

    # Example usage:
    # Construct a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    max_depth = solution.maxDepth(root)
    print(f"Max Depth: {max_depth}")