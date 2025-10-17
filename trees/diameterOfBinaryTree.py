from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    diameter = 0
    dfs(root)
    return diameter

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    tests = [
        root
    ]
    for test in tests:
        print(solve(test))