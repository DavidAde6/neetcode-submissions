# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # BRUTE FORCE - Create a counter, go to the end, figure out distance, go to correct position

        res = head
        start = head
        prev = None
        for i in range(n):
            res = res.next

        while res:
            res = res.next
            prev = start
            start = start.next
        
        if prev:
            prev.next = start.next
        else:
            return start.next

        return head
