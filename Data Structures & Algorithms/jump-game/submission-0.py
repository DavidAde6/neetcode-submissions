class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False for i in range(len(nums) -1) ]
        memo.append(True)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if (j + i) < len(memo) and memo[j + i]:
                    memo[i] = True
        print(memo)
        return memo[0]

        