class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create a memo of same size, set the left and top values from trophy to 1
        # any dp call into those paths can check the memo, and set their values in the memo to that plus 
        #create a memo of same size, set its bottom right to 1

        if m == 1 or n == 1:
            return 1
        memo = [[0 for i in range(n)] for j in range(m)]
        memo[m-1][n-1] = 1

        def dp(r, c):
            if r >= m or c >= n:
                return 0
            if memo[r][c] == 0:
                memo[r][c] = dp(r + 1, c) + dp(r, c + 1)
            return memo[r][c]

        dp(0, 0)
        return memo[0][0]

