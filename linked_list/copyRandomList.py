from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        res = []
        curr = self
        visited = set()
        while curr and curr not in visited:
            visited.add(curr)
            random_val = curr.random.val if curr.random else None
            res.append("{}[{}]".format(curr.val, random_val))
            curr = curr.next

        return "->".join(res)

def solve(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    curr = head
    nodes = {}

    while curr:
        nodes[curr] = Node(curr.val)
        curr = curr.next

    head2 = curr2 = nodes[head]
    curr = head
    while curr:
        curr2.next = nodes[curr.next] if curr.next else None # pyright: ignore[reportOptionalMemberAccess]
        curr2.random = nodes[curr.random] if curr.random else None # pyright: ignore[reportOptionalMemberAccess]

        curr = curr.next
        curr2 = curr2.next # pyright: ignore[reportOptionalMemberAccess]

    return head2


if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2
    n1.random = n2
    n2.random = n2
    
    nn1 = Node(3)
    nn2 = Node(3)
    nn3 = Node(3)
    nn1.next = nn2
    nn2.next = nn3
    nn1.random = None
    nn2.random = nn1
    nn3.random = None
    tests = [ 
        node1,
        n1,
        nn1
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(test)}")
        print("-" * 20)
