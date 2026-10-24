# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        hMap = {}
        # build minHeap, need a dictionary of index, and list heads
        for i, x in enumerate(lists):
            if x:
                hMap[i] = x
                heapq.heappush(minHeap, (x.val, i))
                x = x.next
        
        res = ListNode(0)
        cur = res
        
        # minHeap = (value, index)
        while minHeap:
            # remove from minHeap, add to cur, add its next element to minHeap
            #print(cur.val)
            key = heapq.heappop(minHeap)[1]
            smallest = hMap[key]
            cur.next = smallest
            cur = cur.next

            # add next elem to dict and min Heap
            replacement = smallest.next
            if replacement:
                hMap[key] = replacement
                heapq.heappush(minHeap, (replacement.val, key))
        return res.next

            