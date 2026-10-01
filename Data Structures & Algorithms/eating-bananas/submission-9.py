class Solution:

    def pilecalc(self, hourrate, piles):
        # takes a val, calculates how much needed to clear piles
        result = 0
        for val in piles:
            result += val // hourrate
            if val % hourrate > 0:
                result += 1
        print(str(hourrate) + " - hourrate, result - " + str(result))
        return result

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minVal = 1
        maxVal = max(piles)

        while minVal < maxVal:
            temp = (minVal + maxVal) // 2
            mid = self.pilecalc(temp, piles)
            if (mid > h):
                minVal = temp + 1
            else:
                maxVal = temp
        return minVal
