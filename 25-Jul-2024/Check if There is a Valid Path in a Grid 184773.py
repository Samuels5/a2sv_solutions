# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        d = {1:[(0,1),(0,-1)],2:[(1,0),(-1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def inbound(row, col):
            if 0<=row<rows and 0<=col<cols:
                return True
            return False
        def dfs(row,col):
            if row==rows-1 and col==cols-1:
                return True
            visited.add((row,col))
            for r, c in d[grid[row][col]]:
                newr = row + r
                newc = col +c
                if inbound(newr,newc) and (newr,newc) not in visited and (-r,-c) in d[grid[newr][newc]]:
                    if dfs(newr,newc):
                        return True
        return dfs(0,0)