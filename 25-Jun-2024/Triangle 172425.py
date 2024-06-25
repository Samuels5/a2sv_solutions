# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        
        def dp(r, c):
            if r >= len(triangle):
                return 0
            state = (r, c)
            if state not in memo:
                memo[state] = triangle[r][c] + min(dp(r + 1, c), dp(r + 1, c + 1)) 
            return memo[state]
            
        return dp(0, 0)