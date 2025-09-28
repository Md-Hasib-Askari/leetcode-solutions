from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        r_head = ListNode(head.val)
        c1 = head.next
        c2 = r_head
        n = 1

        while c1:
            c2.next = ListNode(c1.val)
            c1 = c1.next
            c2 = c2.next
            n += 1

        a, b = None, r_head
        c = None
        if r_head and r_head.next:
            c = r_head.next
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        r_head = a

        curr = head
        a = head
        b = r_head
        i = 0
        while i < n // 2:
            a = a.next
            curr.next = b
            curr = curr.next

            if i == n // 2 - 1 and n % 2 == 0:
                break

            b = b.next
            curr.next = a
            curr = curr.next

            i += 1

        curr.next = None


if __name__ == '__main__':
    tests = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
    ]
    s = Solution()
    for t in tests:
        s.reorderList(t)
        while t:
            print(t.val, " -> ", end="")
            t = t.next
        print()