from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        # initial elements
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(res, (l.val, idx, l))

        head = ListNode(-1)
        curr = head
        while res:
            _, idx, node = heapq.heappop(res)

            pnext = node.next
            if pnext:
                heapq.heappush(res, (pnext.val, idx, pnext))

            curr.next = node
            curr = curr.next

        return head.next

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    # Create some example linked lists and merge them
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    
    merged_list = solution.mergeKLists([list1, list2, list3])
    
    # Print the merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")