class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = (len(matrix) + 1) // 2, len(matrix) - 1

        for r in range(ROWS):
            for c in range(r, COLS - r):
                new_r, new_c = r, c
                start = matrix[new_r][new_c]
                for i in range(4):
                    new_r, new_c = new_c, (len(matrix) - 1) - new_r
                    stop = matrix[new_r][new_c]
                    matrix[new_r][new_c] = start
                    start = stop


                