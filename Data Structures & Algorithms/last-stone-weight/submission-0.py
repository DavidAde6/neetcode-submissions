class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #nlogn time
        #n space
        # Loop through the array and find the biggest 2 elements - On^2
        # Add all elements to a heap, remove the 2 biggest, perform the operation and add it back
        # constantly check if array is size 1 or 0, return whats needed as appropriate
        stones = [-stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        while len(stones) > 1:

            l = heapq.heappop(stones)
            r = heapq.heappop(stones)

            heapq.heappush(stones, l - r)
        return -stones[0] if len(stones) == 1 else 0

