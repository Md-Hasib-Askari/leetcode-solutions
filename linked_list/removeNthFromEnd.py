from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        curr = self
        values = []
        while curr:
            values.append(str(curr.val))
            curr = curr.next

        values.append("None")
        return " -> ".join(values)

def solve(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return None
    
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    if n == length == 1:
        return None

    curr = head.next
    p = head
    cn = 1
    while p:
        if cn == length-n+1 == 1:
            return head.next

        if cn == length-n and curr:
            p.next = curr.next

        cn += 1
        p = curr
        if curr:
            curr = curr.next

    return head

if __name__ == "__main__":
    tests = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(1), 1),
        (ListNode(1, ListNode(2)), 1),
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)

        # print(f"Output: {solve(test)}")
        # print("-" * 20)
