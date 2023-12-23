class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for raw in range(len(board)):
            s = set()
            for col in range(len(board[0])):
                if board[raw][col] == '.':
                    continue
                if board[raw][col] in s:
                    return False
                s.add(board[raw][col])
        for col in (zip(*board)):
            s = set()
            for raw in range(9):
                if col[raw] == '.':
                    continue
                if col[raw] in s:
                    return False
                s.add(col[raw])
        
        for raw in [1,4,7]:
            for col in [1,4,7]:
                po=[board[raw-1][col-1],board[raw-1][col],board[raw-1][col+1],board[raw][col-1],board[raw][col],board[raw][col+1],board[raw+1][col-1],board[raw+1][col],board[raw+1][col+1]]
                po1=Counter(po)
                del po1['.']
                for i in po1.values():
                    if i>1:
                        return False
                           
        

        return True
        