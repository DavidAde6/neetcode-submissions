class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [-1 for i in range(len(s))]

        def dp(index):
            if index >= len(s):
                return 1

            if memo[index] == -1:
                if s[index] == "0":
                    memo[index] = 0
                else:
                    memo[index] = dp(index+1)
                    if index < len(s) - 1  and ((s[index] in "2" and s[index+1] in "0123456") or (s[index] in "1")):
                        memo[index] += dp(index+2)
            return memo[index]

        return dp(0)
            
            
            