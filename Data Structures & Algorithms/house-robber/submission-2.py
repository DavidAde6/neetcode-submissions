class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        nums.append(0)
        nums.append(0)

        def dp(index):
            if index >= len(nums) - 4:
                return nums[index]

            if index not in memo:
                memo[index] = nums[index] + max(dp(index+2), dp(index+3))
            return memo[index]

        return dp(-2)

        