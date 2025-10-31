from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    inorder_index = inorder.index(root_val)

    root.left = buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
    root.right = buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])

    return root

# Example usage:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree_root = buildTree(preorder, inorder)

def print_tree(node: Optional[TreeNode], level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.val)
        print_tree(node.left, level + 1)
print_tree(tree_root)
