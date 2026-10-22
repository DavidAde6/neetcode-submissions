class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1, 2, 3, 4, 5, 6] - if right bigger than mid and ans in that range, go right, otherwise
        # [2, 3, 4, 5, 6, 1] - elif mid greater than left and ans in that range go left, otherwise, 
        # check the sequential one, if its theree go therre otherwise
        # if right aint bigger than left, but its in that range
        # [3, 4, 5, 6, 1, 2] - 
        # [4, 5, 6, 1, 2, 3]
        # [5, 6, 1, 2, 3, 4]
        # mid aint bigger than left but its in that range
        # [6, 1, 2, 3, 4, 5]

        # Split it up
        # is right bigger than left, cool, is ans there? go there, is ans bigger go other way
        # is left bigger than mid, 


        # find split, is it bigger or smaller than where split is not, go appropraite place

        # if right > mid, split in left inclusive, is it in range of split? go, no go other way
        # if mid > left, split in right, is it in range of split? go, no other way
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[r] >= nums[mid]:
                # split in left, checking if in regular ranges
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] >= nums[l]:
                # split in rght, check if in left 
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return l if nums[l] == target else -1

