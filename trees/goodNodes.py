class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    res = 0
    max_val = float('-inf')

    def dfs(node: TreeNode, max_val: float):
        if not node: return

        nonlocal res
        if node.val >= max_val:
            res += 1
        max_val = max(max_val, node.val)
        if node.left:
            dfs(node.left, max_val)
        if node.right:
            dfs(node.right, max_val)

    dfs(root, max_val)
    return res

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.right = TreeNode(5)
    root1.right.left = TreeNode(1)

    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)


    root3 = TreeNode(1)

    tests = [ root1, root2, root3 ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
