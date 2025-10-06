from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        res = []
        curr = self
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return "->".join(res)

def solve(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    d1 = 0
    d2 = 0

    curr = l1
    c = 0
    while curr:
        d1 += (curr.val * 10**c)
        curr = curr.next
        c += 1

    curr = l2
    c = 0
    while curr:
        d2 += (curr.val * 10**c)
        curr = curr.next
        c += 1
    
    res = str(d1 + d2)
    head = curr = ListNode(-1)
    for i in range(len(res)-1, -1, -1):
        d = int(res[i])
        node = ListNode(d)
        curr.next = node
        curr = curr.next
    curr.next = None

    return head.next






if __name__ == "__main__":
    tests = [
        (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))),
        (ListNode(0), ListNode(0)),
        (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
    ]
    for test in tests:
        print(f"Input: {test}")
        print(f"Output: {solve(*test)}")
        print("-" * 20)
