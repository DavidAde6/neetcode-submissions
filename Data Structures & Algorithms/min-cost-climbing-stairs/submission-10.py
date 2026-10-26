class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {len(cost) - 1: cost[len(cost) -1], len(cost) - 2: cost[len(cost) - 2]}

        def dp(index):
            if index in memo:
                return memo[index]

            memo[index] = cost[index] + min(dp(index+1), dp(index+2))
            return memo[index]



        return min(dp(0), dp(1))
