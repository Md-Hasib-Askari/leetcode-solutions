class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def solve(root: 'TreeNode', p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if curr.val < p.val and curr.val < q.val:
            curr = curr.right
        elif curr.val > p.val and curr.val > q.val:
            curr = curr.left
        else:
            return curr
    
    return root

if __name__ == "__main__":
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)

    tests = [ 
        (root1, TreeNode(2), TreeNode(8)),  # Expected output: TreeNode(6)
        (root1, TreeNode(2), TreeNode(4)),  # Expected output: TreeNode(2)
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test).val}")
        print("-" * 20)
