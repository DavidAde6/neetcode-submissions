# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ez af, just go left to right, build each number, add then parse back tf
        n1 = 0
        n2 = 0
        count = 1
        while l1 or l2:
            if l1:
                n1 += (count * l1.val)
                l1 = l1.next
            if l2:
                n2 += (count * l2.val)
                l2 = l2.next
            count *= 10

        resNum = n1 + n2
        resHead = ListNode()
        cur = resHead

        while resNum > 0:
            cur.val = resNum % 10
            print(cur.val)
            resNum //= 10
            if resNum == 0:
                break
            cur.next = ListNode()
            cur = cur.next


        return resHead