from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root: return res

    q = collections.deque()
    q.append(root)

    while q:
        lis = []
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                lis.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if lis:
            res.append(lis[-1])

    return res

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)

    tests = [
        root1,
        root2,
        None
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
