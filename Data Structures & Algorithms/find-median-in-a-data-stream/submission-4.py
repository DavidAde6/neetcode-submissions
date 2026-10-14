class MedianFinder:

    def __init__(self):
        self.heapleast = []
        self.heapmost = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heapmost, num)
        #print(self.heapleast, self.heapmost)
        if len(self.heapmost) - len(self.heapleast) >= 2:
            dummy = heapq.heappop(self.heapmost)
            heapq.heappush(self.heapleast, -dummy)
        if len(self.heapleast) - len(self.heapmost) >= 2:
            dummy = heapq.heappop(self.heapleast)
            heapq.heappush(self.heapmost, -dummy)
        if len(self.heapleast) > 0 and self.heapmost[0] < -(self.heapleast[0]):
            dummyMost = heapq.heappop(self.heapmost)
            dummyLeast = -heapq.heappop(self.heapleast)
            #print(self.heapleast, self.heapmost)
            heapq.heappush(self.heapmost, dummyLeast)
            heapq.heappush(self.heapleast, -dummyMost)


    def findMedian(self) -> float:
        # if heapmost + heapleast is odd, return heapmost[0]
        # else return heapmost[0] + -heapleast[0] / 2
        #print(self.heapleast, self.heapmost)
        if len(self.heapmost) + len(self.heapleast) == 0:
            return 0.0
        if (len(self.heapmost) + len(self.heapleast)) % 2 == 1:
            return float(self.heapmost[0])
        return (self.heapmost[0] + (-self.heapleast[0])) / 2.0