from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solve(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    old_to_new = {}

    def dfs(n: 'Node') -> 'Node':
        if n in old_to_new:
            return old_to_new[n]

        copy = Node(n.val)
        old_to_new[n] = copy

        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    n11 = Node(1)
    
    tests = [
        n1, n11, None
    ]

    # print("Cloned Graphs:")
    def print_graph(node: Optional['Node']):
        if not node:
            print("None")
            return
        visited = set()
        def dfs(n: 'Node'):
            if n in visited:
                return
            visited.add(n)
            print(f"Node {n.val} with neighbors {[neighbor.val for neighbor in n.neighbors]}")
            for neighbor in n.neighbors:
                dfs(neighbor)
        dfs(node)

    for test in tests:
        print(f"Input: {test}")
        # print(f"Output: {solve(test)}")
        graph_copy = solve(test)

        # print("-" * 20)
        print("Original Graph:")
        print_graph(test)
        print("Cloned Graph:")
        print_graph(graph_copy)
        print()