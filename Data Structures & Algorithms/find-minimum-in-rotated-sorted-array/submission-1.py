class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1]

        # if bigger than or equal to both min on the right else, include mid in left


        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]