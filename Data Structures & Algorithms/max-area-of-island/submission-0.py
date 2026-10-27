class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # loop through the array, once a 1 has been found, call dfs, find everything, turn to 0, return count
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        self.count = 0
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return

            self.count += 1
            grid[r][c] = 0
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.count = 0
                    dfs(r, c)
                    res = max(res, self.count)
        
        return res
