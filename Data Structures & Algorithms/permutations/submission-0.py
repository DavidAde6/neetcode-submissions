class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for each element print itself then recursively call rest of elements

        res = []

        # from [2,3] to [1]
        # if not full, add all elements starting from 1 element from from to to
        # do that till from is empty
        # add them back, 

        def dfs(fro, to):
            #print(to)
            if len(to) == len(nums):
                res.append(to[:])
                return
            for i, num in enumerate(fro):
                dfs(fro[:i] + fro[i+1:], to + [num])


        dfs(nums, [])
        return res