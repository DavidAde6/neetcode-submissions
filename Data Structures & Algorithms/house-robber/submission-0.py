class Solution:
    def rob(self, nums: List[int]) -> int:
        [1, 1, 3, 3, 0, 0]
        [4, 4, 3, 3]
        # 1    3
        # 1       3
        #   1     3
        # at a given index, you can either take the 2nd closest or the third closest
        # i append 2 0's to the nums array, and start my loop at index -2
        # then we check, starting from index 0 and 1, and return the max + its value

        # if we are at the last two indexes, which would be positions -3 and -4
        # we return its value, and add it to the memo

        memo = {}
        nums.append(0)
        nums.append(0)

        #[1, 1, 3, 3, 0, 0]
        #[4, 4, 3, 3]

        def dp(index):
            if index >= len(nums) - 4:
                return nums[index]

            if index not in memo:
                memo[index] = nums[index] + max(dp(index+2), dp(index+3))
            return memo[index]

        return dp(-2)

        