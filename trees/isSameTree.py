from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    p_nodes = []
    q_nodes = []
    def traversal(node: Optional[TreeNode], nodes: list[Optional[int]]):
        if not node:
            nodes.append(None)
            return
        
        nodes.append(node.val) # pre-order traversal (works)
        traversal(node.left, nodes)
        # nodes.append(node.val) # in-order traversal (doesn't work as symmetric)
        traversal(node.right, nodes)
        # nodes.append(node.val) # post-order traversal (works too)

    traversal(p, p_nodes)
    traversal(q, q_nodes)

    print(p_nodes)
    print(q_nodes)

    if len(p_nodes) != len(q_nodes):
        return False

    for i in range(len(p_nodes)):
        if p_nodes[i] != q_nodes[i]:
            return False
    
    return True 

if __name__ == "__main__":
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    p4 = TreeNode(2)
    p4.left = TreeNode(2)
    p4.right = TreeNode(2)
    p4.left.right = TreeNode(2)
    p4.left.right.left = TreeNode(2)
    q4 = TreeNode(2)
    q4.left = TreeNode(2)
    q4.right = TreeNode(2)
    q4.left.left = TreeNode(2)
    q4.right.left = TreeNode(2)
    tests = [(p1, q1), (p2, q2), (p3, q3), (p4, q4)]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
