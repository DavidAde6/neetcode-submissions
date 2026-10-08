class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        currIteratingArray = []
        
        def calculate(arr, start):
            if sum(arr) == target:
                result.append(arr.copy())
                return
                
            if sum(arr) > target:
                return

            for i in range(start, len(nums)):
                elem = nums[i]
                arr.append(elem)
                calculate(arr, i)
                arr.pop()
            return

        calculate(currIteratingArray, 0)
        return result


