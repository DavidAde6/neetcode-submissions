class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1 for i in range(amount + 1)]
        memo[0] = 0
        def dp(num):
            if memo[num] > -1:
                return memo[num]

            cur = float('inf')
            for coin in coins:
                if num - coin < 0:
                    continue
                new = dp(num - coin) + 1
                cur = min(cur, new)
            memo[num] = cur 
            return memo[num] 

        res = dp(amount)
        return res if res != float('inf') else -1


        