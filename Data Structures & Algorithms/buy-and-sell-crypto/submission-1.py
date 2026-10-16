class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want more pizza
        # ok, we want max(r - l), 
        # l r pointer
        # l pointer is the absolu minimumn, r pointer is a mova
        # l can jump to rs position if it feel like gaingstaa footera
        
        l = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            r = prices[i]
            if r - l <= 0 and r < l:
                #print(r)
                l = r

            #print(l, r)
            maxProfit = max(maxProfit, r - l)
            #print(maxProfit)
            r += 1

        return maxProfit