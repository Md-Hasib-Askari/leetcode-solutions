from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    def check_balance(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_height = check_balance(node.left)
        right_height = check_balance(node.right)
        if left_height == -1 or right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    return check_balance(root) != -1

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)

    tests = [root1, root2]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
