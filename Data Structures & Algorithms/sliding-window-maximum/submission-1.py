class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force is to do it
        # issue is we are computing k-1 elements we've already computed
        # need to find a way to just compute the new values with something, the leftovers, so we pop from an array, and the array gives us the max

        # lets say we add an element, its the biggest, so for the next k turns, if nothing bigger comes, its still the biggest so we compare it with the next couple elements
        # so we use a heap, but not in the way u think

        # lets say we have 4 as biggest
        # 2 comes, 4 is biggest, 


        # first approach pretty much a heap with inefficient remove

        # max 2, check if 2 is still in window, compare 2 with new element. 
        # is new element bigger, remove 2, if 2 is not in window, heapify
        # do that till end

        res = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        for i in range(k, len(nums)):
            #print(nums[i], -nums[i])
            heapq.heappush(heap, (-nums[i], i))
            #print(heap)
            while heap[0][1] < (i - k) + 1: # 0 < 1 - 1 
                heapq.heappop(heap)
            #print(heap)
            res.append(-heap[0][0])
        return res
            

