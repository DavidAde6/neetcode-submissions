class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [16 ,18 ,22, 21, 20]
        # we check for 20, nothing to right, so 0
        # we check if 21 is smaller than 20, no so 0, this also tells us that if anything is bigger than 21 to the left, it wont find a match, so we make 21 curr max, we store the val and the index
        # we go to 22, its bigger than curr max so nothing bigger follows, 
        # we can implement it like this
        # we can also further create more potential maxes, abs max is 22, next is 18, then 16

        currMax = temperatures[-1]
        currIndex = len(temperatures) - 1
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] >= currMax:
                currIndex = i
                currMax = temperatures[i]
            else:
                for j in range(i, currIndex + 1):
                    if temperatures[j] > temperatures[i]:
                        res[i] = j - i
                        break
        return res



