# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}

        def inbound(r, c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

        def dp(r, c):
            if not inbound(r, c) or matrix[r][c] == '0':
                return 0

            state = (r, c)
            if state not in memo:
                memo[state] = 1 + min(dp(r, c + 1), dp(r + 1, c), dp(r + 1, c + 1))
                
            return memo[state]
            
        maxi = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    maxi = max(dp(row, col), maxi)

        return maxi ** 2