from typing import List, Optional
import collections

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) ->  List[List[int]]:
    res = []
    if not root: return res
    
    q = collections.deque()
    q.append(root)

    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)

    return res

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(1)

    root3 = None
    tests = [root1, root2, root3]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
