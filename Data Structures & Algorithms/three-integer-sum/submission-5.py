class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer still?
        nums.sort()
        result = []
        for i,x in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + x == 0:
                    a = sorted([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    if a not in result:
                        result.append(a)
                    if len(result) == 0:
                        result.append(a)
                    pass
                elif nums[l] + nums[r] + x < 0:
                    l += 1
                else:
                    r -= 1
        return result