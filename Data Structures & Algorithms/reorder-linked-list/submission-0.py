# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        s = head
        f = head.next
        while f:
            s = s.next
            f = f.next
            if f: 
                f = f.next
        prev = None
        
        while s:
            nxt = s.next 
            s.next = prev 
            prev = s 
            s = nxt 
        
        start = head
        stop = prev
        
        while start or stop:
            if start:
                nxt = start.next
                start.next = stop
                start = nxt
            if stop:
                nxt = stop.next
                stop.next = start
                stop = nxt



