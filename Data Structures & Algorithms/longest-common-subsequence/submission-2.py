class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        t1 = len(text1)
        t2 = len(text2)
        dp = [[0 for i in range(t1 + 1)] for j in range(t2 + 1)]

        for r in range(t2-1, -1, -1):
            for c in range(t1-1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0]