class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the area is the (r - l) times min(heights[r], heights[l])
        # start at the ends
        # when to move l when to move r, best to not go back
        # start at ends. if u m
        # max length - 8
        #[1, 9, 17, 4, 4, 7, 15, 2, 6]
        # 8, 42, 18, 45, 
        # you try moving to the right, you get a bigger value.
        # it was 1 height before, but because it can never be bigger, because 1 * any closer distance is smaller than current
        # you then try 7 and 6, min of which is 6, you know if its 

        # if l is bigger than r or vice versa, move the smaller, if theyre equal move both
        l = 0
        r = len(heights) - 1
        currMax = 0
        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            currMax = max(currMax, currArea)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
                r -= 1
        
        return currMax
