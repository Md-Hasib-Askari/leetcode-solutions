from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     def reverse_linked_list(start: ListNode, end: ListNode) -> ListNode:
    #         prev = None
    #         current = start
    #         while current != end:
    #             next_node = current.next
    #             current.next = prev
    #             prev = current
    #             current = next_node
    #         return prev

    #     dummy = ListNode(0)
    #     dummy.next = head
    #     group_prev = dummy

    #     while True:
    #         kth = group_prev
    #         for _ in range(k):
    #             kth = kth.next
    #             if not kth:
    #                 return dummy.next
            
    #         group_next = kth.next
    #         # Reverse the group
    #         prev, curr = kth.next, group_prev.next
    #         while curr != group_next:
    #             temp = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = temp
            
    #         temp = group_prev.next
    #         group_prev.next = kth
    #         group_prev = temp

    #     return dummy.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head

        for _ in range(k):
            if not temp:
                return head
            
            temp = temp.next

        prevNode = self.reverseKGroup(temp, k)

        p = head
        for _ in range(k):
            temp = p
            p = p.next if p else None
            if temp:
                temp.next = prevNode
            prevNode = temp
        
        return prevNode

    
# Example usage:
# Constructing the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
solution = Solution()
new_head = solution.reverseKGroup(head, k)

# Printing the reversed linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
