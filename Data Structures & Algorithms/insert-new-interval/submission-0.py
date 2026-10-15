class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        currIv = newInterval    

        # [1, 2] [3, 5] [9, 10] [11, 12] 
        # currIv []
        # res [[1, 2], [3, 5], [6, 7], [9, 10]]

        for iv in intervals:
            if currIv:
                if currIv[1] < iv[0]:
                    res.append(currIv[:])
                    currIv = []
                    res.append(iv)
                elif currIv[0] > iv[1]:
                    res.append(iv)
                else:
                    currIv[0] = min(currIv[0], iv[0])
                    currIv[1] = max(currIv[1], iv[1])
            else:
                res.append(iv)

        if currIv:
            res.append(currIv[:])
        return res