class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # using for loop search until a start char is found, if yes, call dfs function
        # dfs, we pass in index in word (0) and board pos [r][c]
        # create a hashset of visited positions
        # call dfs on each 4 appended on its call, if valid, call again, if not return
        #
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(index, r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or board[r][c] != word[index] or (r, c) in visited:
                return False
            if index == len(word) - 1 and board[r][c] == word[index]:
                return True
            visited.add((r, c))
            retVal = dfs(index+1,r-1,c) or dfs(index+1,r+1,c) or dfs(index+1,r,c+1) or dfs(index+1,r,c-1)
            visited.remove((r, c))
            return retVal

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        return False
                    
            