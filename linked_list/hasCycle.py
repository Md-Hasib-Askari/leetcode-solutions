from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            if slow is None or slow.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

if __name__ == '__main__':
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    # l4.next = l2
    # l3.next = l4
    # l1.next = l2
    # l2.next = l1
    tests = [
        [l1]
    ]
    s = Solution()
    for t in tests:
        print(s.hasCycle(*t))