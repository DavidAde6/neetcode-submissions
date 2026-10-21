class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # create an array of first and last elements, 
        # if number is between odd -> even, check within, if even -> odd, not
        # or check left most values and fit in as appropriate, 

        # lets do latter, less complex
        # binary search on first elem, binary search on alst elem

        # treat it like a 1d

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l < r:
            mid = l + (r - l) // 2
            outer = mid // len(matrix[0])
            inner = mid % len(matrix[0])

            if matrix[outer][inner] == target:
                return True

            if matrix[outer][inner] > target:
                r = mid - 1
            else:
                l = mid + 1

        outer = l // len(matrix[0])
        inner = l % len(matrix[0])
        return matrix[outer][inner] == target