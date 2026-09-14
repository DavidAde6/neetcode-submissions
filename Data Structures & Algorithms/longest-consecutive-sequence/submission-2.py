class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        curr = 0
        result = 0
        if len(nums) == 0:
            return 0
        # as you go, if its not one more than the previous
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                curr += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                if curr > result:
                    result = curr
                curr = 0
        if curr > result:
            result = curr             
        return result + 1
