class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # "aab"
        # ['a', 'a', 'b'] end of list, add to result
        # ['aa', ]
        # ['aab']
        # inner dfs with for loop

        # dfs gives you an index
        # if index >= len(s) add to res and return
        # for loop from index, to len(s)
        # if s[index:i+1] == its reverse, add to cur array, and call function with dfs(i+1)
        # if its not a palindrome, keep going.

        res = []
        self.cur = []

        def dfs(index):
            if index >= len(s):
                res.append(self.cur[:])
                return

            for i in range(index, len(s)):
                candidate = s[index:i+1]
                if candidate == candidate[::-1]:
                    self.cur.append(candidate)
                    dfs(i+1)
                    self.cur.pop()
        
        dfs(0)
        return res