# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        direction = [(1,0),(0,1)]
        memo = {}
        if obstacleGrid[0][0] == 1:
            return 0
            
        def inbound(r, c): 
            return 0 <= r < len(obstacleGrid) and 0 <= c < len(obstacleGrid[0])

        def dp(row,col):
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                return 1
            state = (row, col)
            if state not in memo:
                val = 0
                for r, c in direction:
                    nr, nc = r + row, c + col
                    if inbound(nr, nc) and obstacleGrid[nr][nc] != 1:
                        val += dp(nr, nc)
                memo[state] = val
            return memo[state]

        return dp(0, 0)