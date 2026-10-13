# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #gonna have 2 pointers 
        # if the same, go with left
        # if left is bigger go with right
        # if at end, go with other

        # ok, start at 2 1's
        # theyre equal select the left 1
        # create a curr, and temp set it point to the left 1
        # move the left one to next element
        # choose min again, 

        # start with minimum between left and right
        #curr = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1


        if list1.val < list2.val:
            curr = list1
            res = curr
            list1 = list1.next
        else:
            curr = list2
            res = curr
            list2 = list2.next

        print(curr.val)
            

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1 is None:
            curr.next = list2
        elif list2 is None:
            curr.next = list1

        return res
            