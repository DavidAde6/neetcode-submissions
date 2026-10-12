class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        [9, 1, 4, 2, 3, 3, 7, 10]
        [0, 0, 0, 0, 0, 0, 0]


        9
        # currMax = 0 initialized inside the dp, like first line
        # dp goes through the array until it finds an element bigger
        # when it does it finds the max length of that combination, it compares that with currMax, if its bigger, we set it to currMax, if not keep going.
        # when its done, it gets added to memo for its index, and returned
        # we are calling dp on the position, meaning once its max has been found,
        # if that is bigger than currMax, it becomes currMax
        # if we go to a new index in our for loop we check if its in memo, if it is we dont need to call dp, we just get the value, if not thats when we call dp.
        memo = {}
        def dfs(index):
            if index == len(nums):
                return 1

            currSum = 0
            # we are at an index, we are checking every following element to see what the biggest is
            # if were at last index, we should return 1 + 0 somehow
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    if i not in memo:
                        # we call the dfs function which returns the biggest
                        memo[i] = dfs(i)
                    currSum = max(currSum, memo[i])
            memo[index] = currSum + 1
            return memo[index]
            # once we figured out the max array

        for i in range(len(nums)):
            dfs(i)
        print(memo)
        return max(memo.values())



