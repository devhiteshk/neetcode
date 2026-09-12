class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0 - 3, 2 - 6, 4 - 9 - r
        # 0 - 3, 2 - 6, 4 - 9 - c

        rc = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in rc:
                    return False
                elif board[i][j] != ".":
                    rc.add(board[i][j])
            rc = set()

        rc = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[j][i] in rc:
                    return False
                elif board[j][i] != ".":
                    rc.add(board[j][i])
            rc = set()

        sr = 0
        sc = 0
        r = 3
        c = 3
        x = set()

        while r <= 9 and j <= 9:
            for i in range(sr, r):
                for j in range(sc, c):
                    if board[i][j] in x:
                        return False
                    elif board[i][j] != ".":
                        x.add(board[i][j])  
            x = set()

            sc = c
            c += 3

            if c > 9:
                sc = 0
                c = 3
                sr = r
                r += 3

        return True