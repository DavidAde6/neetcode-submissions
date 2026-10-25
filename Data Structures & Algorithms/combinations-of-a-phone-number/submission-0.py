class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs takes an index and cur, if index is len(digits) return
        # digits[i] appropriate values gotten from a hashmap, store it locally
        # in a for loop call each char from map to that string plus that, and increment index

        res = []
        digMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}

        if len(digits) == 0:
            return []

        def dfs(index, cur):
            if index == len(digits):
                res.append(cur)
                return
            candidates = digMap[digits[index]]
            for char in candidates:
                dfs(index + 1, cur + char)
        
        dfs(0, "")
        return res

            