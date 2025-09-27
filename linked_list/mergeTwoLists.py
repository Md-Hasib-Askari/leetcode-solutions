from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f'{self.val} -> {self.next}' if self.next else f'{self.val}'

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        p, pc1, pc2 = None, list1, list2
        head = None
        if pc1.val <= pc2.val:
            head, p = pc1, pc1
            pc1 = pc1.next
        else: 
            head, p = pc2, pc2
            pc2 = pc2.next

        while pc1 and pc2:
            if pc1.val <= pc2.val:
                p.next = pc1
                pc1 = pc1.next
            else:
                p.next = pc2
                pc2 = pc2.next
            p = p.next

        if pc1:
            p.next = pc1
        if pc2:
            p.next = pc2
        return head

if __name__ == '__main__':
    tests = [
        (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))),
        (ListNode(1, ListNode(2, ListNode(4))), None),
        (None, ListNode(1, ListNode(3, ListNode(4)))),
        (None, None),
    ]
    s = Solution()
    for t in tests:
        res = s.mergeTwoLists(*t)
        while res:
            print(res.val, end=' -> ' if res.next else '\n')
            res = res.next