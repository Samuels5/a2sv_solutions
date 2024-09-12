# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def inbound(r,c): return 0 <= r <len(grid1) and 0 <= c < len(grid1[0])
        dirc = [(-1,0),(1,0),(0,1),(0,-1)]
        s = set()
        def dfs(raw,col):
            x = True
            s.add((raw,col))
            for r,c in dirc:
                nr = raw + r
                nc = col + c
                if inbound(nr,nc) and grid2[nr][nc] == 1 and (nr,nc) not in s:
                    if grid1[nr][nc] == 0:
                        x = False
                    x = dfs(nr,nc) and x

            return x

        count = 0
        for raw in range(len(grid1)):
            for col in range(len(grid1[0])):
                if (raw,col) not in s and grid2[raw][col] == 1 and grid1[raw][col] == 1:
                    if dfs(raw,col):
                        print(raw,col)
                        count += 1
                    
                        
        return count
