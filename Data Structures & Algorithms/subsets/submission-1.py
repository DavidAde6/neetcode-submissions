class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # yk the drill, go down, left means at a 1, go down right means add a []

        # inner func, base case, if not call func on adding new stuff and not 
        outputArr = []
        def getSubset(depth, arr):
            if depth == len(nums):
                outputArr.append(arr[:])
                return 
            
            arr.append(nums[depth]) 
            getSubset(depth + 1, arr)
            arr.pop()
            print("depth: ", depth + 1, " arr: ", arr)
            getSubset(depth + 1, arr)

            

        getSubset(0, [])
        return outputArr