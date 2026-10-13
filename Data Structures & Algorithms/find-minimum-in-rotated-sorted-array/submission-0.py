class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if mid > l and r mimimum is in second half, so we cut out first
        # else its in first half including the middle
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            print(l, r)
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            

        return nums[l]