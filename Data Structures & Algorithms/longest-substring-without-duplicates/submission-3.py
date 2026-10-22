class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring of unique characters
        # l and r obs
        # xxxx - check if 2 strings count, no? next elem
        # abcabc  -same approach
        # abcbabc
        # a.d.a.d

        # pain in the ass -> checking whether its in array, use a set()
        chars = {}
        curMax = 0
        l = 0
        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = i
            else:
                #print(c, "(", i,") " "is in ", chars)
                rem = chars[c]
                while l <= rem:
                    #print("l: ", l, s[l])
                    chars.pop(s[l])
                    l += 1
                chars[c] = i
            curMax = max(len(chars), curMax)
        return curMax


