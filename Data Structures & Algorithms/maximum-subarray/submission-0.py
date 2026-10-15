class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prevMax = float('-inf')
        maxSum = prevMax
        for num in nums:
            prevMax = max(prevMax + num, num)
            maxSum = max(maxSum, prevMax)
        return maxSum
