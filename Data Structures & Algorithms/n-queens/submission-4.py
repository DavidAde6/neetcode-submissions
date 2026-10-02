class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # like sudoku, one per row
        # very similar to last problem

        # for i in range(n) - loop through 2d array length
        # each loop is starting at the top. meaning first iteration is a queen at the top, lets say top corner, its possible none is found with queen here
        # in for loop, you call inner function. 
        # it places the first queen somewhere. its position should be identified in a global 2d array so it knows where not to go.
        # once a good spot has been found, it gets added to curr arr, and the banned array, 
        # if len cur itr array is equal or greater than len n. add copy to result, then return
        # before calling the func within itself, pop from curitrarray and currbannedarray. 
        # u dont need to acocunt for diagonals, but u need to account for king like positions

        result = []
        currItrArray = []
        currBannedArray = []

        def innerRecurs(arr):
            if len(arr) >= n:
                result.append(arr.copy())
                return

            for i in range(n):
                string = ""
                # build string
                for j in range(n):
                    if j == i:
                        string += "Q"
                    else:
                        string += "."

                # banned array and reg array add
                # reg array - works if banned array says good
                
                if bannedArrayAdd(i):
                    arr.append(string)
                    innerRecurs(arr)
                    arr.pop()
                    currBannedArray.pop()


        def bannedArrayAdd(col):
            # takes an int, if int exists not in banned array, it doesn't collide vertically, and if most recent int is not within -1 and +1 then good
            row = len(currBannedArray) - 1
            if len(currBannedArray) <= 0:
                currBannedArray.append((row, col))
                return True

            for elem in currBannedArray:
                if elem[1] == col:
                    return False

                # check if diagonal
                # 1 1 - 3 3, 1 4 - 3 6
                if abs(row - elem[0]) == abs(col - elem[1]):
                    return False


            currBannedArray.append((row, col))
            return True


        innerRecurs(currItrArray)
        return result
