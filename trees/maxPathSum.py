from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    res = float('-inf')
    def dfs(node: Optional[TreeNode]):
        if not node: return float('-inf')

        nonlocal res
        left = dfs(node.left)
        right = dfs(node.right)
        left = max(left, 0)
        right = max(right, 0)

        res = max(res, left + right + node.val)

        return max(left, right) + node.val

    dfs(root)
    return 0 if res == float('-inf') else int(res)

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)

    tests = [root1, root2]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
