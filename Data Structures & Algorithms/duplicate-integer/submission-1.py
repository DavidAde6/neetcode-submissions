class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        l = 0
        for i in range(len(nums)):
            temp.add(nums[i])
            l += 1
            if l > len(temp):
                return True
        return False 
        