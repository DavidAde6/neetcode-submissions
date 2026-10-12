from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {}
        def dfs(i):
            if i > len(cost) - 3:
                return cost[i]
            if i not in memo:
                memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]


        return dfs(-1)