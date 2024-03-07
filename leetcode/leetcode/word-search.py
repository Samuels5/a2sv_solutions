class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []
        size = len(word)
        val = []
        flag1 = 0

        for raw in range(len(board)):
            for col in range(len(board[0])):
                if board[raw][col] == word[0]:
                    flag1 = 1
                    val.append([raw,col])
        def back(raw,col,i):
            if i == size: return True
            
            if raw+1 < len(board) and word[i] == board[raw+1][col] and [raw+1,col] not in stack:
                stack.append([raw+1,col])
                if back(raw+1,col,i+1):
                    return True
                stack.pop()
            if raw-1>=0 and word[i] == board[raw-1][col] and [raw-1,col] not in stack:
                stack.append([raw-1,col])
                if back(raw-1,col,i+1):
                    return True
                stack.pop()
            if col+1 < len(board[0]) and word[i] == board[raw][col+1] and [raw,col+1] not in stack:
                stack.append([raw,col+1])
                if back(raw,col+1,i+1):
                    return True
                stack.pop()
            if col-1 >= 0 and word[i] == board[raw][col-1] and [raw,col-1] not in stack:
                stack.append([raw,col-1])
                if back(raw,col-1,i+1):
                    return True
                stack.pop()

        for raw,col in val:
            stack.append([raw,col])
            if back(raw,col,1):
                return True
            stack.pop()
        return False
        