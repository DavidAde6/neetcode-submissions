class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        size = 0

        for c in range(len(s)):
            for i in [c, c+1]:
                l = c
                r = i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    #print(s[l], s[r])
                    l -= 1
                    r += 1
                    cur_size = r - l + 1
                if cur_size > size:
                    res = s[l+1:r]
                    size = cur_size

        return res