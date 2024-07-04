# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        direction = [(1,-1),(1,0),(1,1)]
        sumi = 0
        num = inf
        memo = {}

        def inbound(r, c):
            return 0 <= r < len(matrix) and 0 <= c <len(matrix[0])
        
        def dp(row, col):
            state = (row, col)
            if state not in memo:
                if row == len(matrix) - 1:
                    return 0
                val = inf

                for r, c in direction:
                    nr, nc = row + r, col + c
                    if inbound(nr, nc):
                        val = min(dp(nr, nc) + matrix[nr][nc], val)
                        
                memo[state] = val

            return memo[state]

        for i in range(len(matrix[0])):
            num = min(dp(-1,i), num)

        return num