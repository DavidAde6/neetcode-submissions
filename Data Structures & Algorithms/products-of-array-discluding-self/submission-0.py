class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 times 2 is needed by 4, 6 so save that
        # product times 4 is needed by 6
        prearr = [1 for i in range(len(nums))]
        postarr = [1 for i in range(len(nums))]
        result = []
        for i in range(len(nums)):
            if i == 0:
                prearr[i] = 1
            else:
                prearr[i] = prearr[i-1] * nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postarr[i] = 1
            else:
                postarr[i] = postarr[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result.append(prearr[i] * postarr[i])
        return result

