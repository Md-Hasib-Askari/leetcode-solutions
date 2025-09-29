from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            if not slow:
                break
            slow = slow.next
            fast = fast.next.next
    
        # Reverse the second half
        second_half = slow.next
        prev = slow.next = None
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        # Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

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