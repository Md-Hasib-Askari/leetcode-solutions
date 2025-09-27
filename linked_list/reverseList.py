from typing import Optional

# Definition for singly-linked list.
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
        return " -> ".join(res) + " -> None"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head
        while b:
            c = b.next
            b.next = a
            a = b
            b = c

        return a

if __name__ == '__main__':
    tests = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))),
        ListNode(1, ListNode(2, None)),
        None
    ]

    s = Solution()
    for t in tests:
        res = s.reverseList(t)
        print(res)