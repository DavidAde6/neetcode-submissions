class Solution:
    def search(self, nums: List[int], target: int) -> int:
        curr = int(len(nums) / 2)
        prevcurr = -10001
        start = 0
        end = len(nums)
        while nums[curr] != target:
            if nums[curr] > target:
                end = int((end + start) / 2)
                curr = int((end + start) / 2)
            elif nums[curr] < target:
                start = int((end + start) / 2)
                curr = int((end + start) / 2)
            if curr == prevcurr:
                return -1
            prevcurr = curr
        return curr