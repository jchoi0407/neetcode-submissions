class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] != ".": 
                    if board[i][j] in row:
                        return False
                    else: 
                        row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    else: 
                        col.add(board[j][i])

        for r_start in range(0, 9, 3):
            # Loop through the top-left corner column of each box (0, 3, 6)
                for c_start in range(0, 9, 3):
                    box = set()
                    
                    # Scan the 3x3 cells inside this specific box block
                    for r in range(r_start, r_start + 3):
                        for c in range(c_start, c_start + 3):
                            val = board[r][c]
                            if val != ".":
                                if val in box:
                                    return False
                                box.add(val)
                
        return True
        


                
            



            



        