from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root        

if __name__ == "__main__":
    solution = Solution()

    # Example usage:
    # Construct a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    inverted_root = solution.invertTree(root)
    # Function to print the tree in-order for verification
    def print_inorder(node):
        if node:
            print_inorder(node.left)
            print(node.val, end=' ')
            print_inorder(node.right)
            
    print_inorder(inverted_root)