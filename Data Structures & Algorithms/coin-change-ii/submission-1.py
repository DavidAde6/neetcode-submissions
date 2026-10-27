class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #coins.sort(reverse=True)

        memo = {(0, i): 1 for i in range(len(coins))}

        def dp(amount, coin):
            if amount < 0 or coin >= len(coins):
                return 0

            if (amount, coin) in memo:
                return memo[(amount, coin)]
            #print(coin)
            memo[(amount, coin)] = dp(amount, coin+1) + dp(amount-coins[coin], coin)
            return memo[(amount, coin)]

        return dp(amount, 0)

    

