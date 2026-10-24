class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        cur = []
        def dfs(num, index): 
            if index == len(candidates):
                return
            for i in range(index, len(candidates)):
                if candidates[i] == candidates[i-1] and i > index:
                    continue
                newNum = num + candidates[i] 
                cur.append(candidates[i])
                if newNum == target:
                    res.append(cur[:])
                elif newNum < target:
                    dfs(newNum, i+1)
                cur.pop()

        dfs(0, 0)
        return res