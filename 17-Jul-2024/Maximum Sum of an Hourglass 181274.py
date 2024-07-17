# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi=0

        for raw in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                sumi=grid[raw][col]+grid[raw][col+1]+grid[raw][col+2]+grid[raw+1][col+1]+grid[raw+2][col]+grid[raw+2][col+1]+grid[raw+2][col+2]
                if sumi>maxi:
                    maxi=sumi
                    
        return maxi