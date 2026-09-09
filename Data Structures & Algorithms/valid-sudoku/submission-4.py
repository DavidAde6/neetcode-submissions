class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = []
        for b in board:
            for c in b:
                if c != ".":
                    temp.append(c)
            s = set(temp)
            if len(s) < len(temp):
                print(len(s), len(temp))
                return False
            temp = []
        print("1")
        temp = []
        for i in range(9):
            for j in range(9):
                c = board[j][i]
                if c != ".":
                    temp.append(c)
                    print("C = ", c)
            s = set(temp)
            print(temp)
            if len(s) < len(temp):
                return False
            temp = []
        temp = []
        print("2")
        for i in range(3): #3 rows down
            for j in range(3):# 3 rows left
                for k in range(3):# per 3 rows 1 row down
                    for l in range(3):# per 3 rows 1 row left
                        if board[(3*i) + k][(3*j) + l] != ".":
                            temp.append(board[(3*i) + k][(3*j) + l])
                s = set(temp)
                if len(s) < len(temp):
                    return False
                temp = []
        return True
