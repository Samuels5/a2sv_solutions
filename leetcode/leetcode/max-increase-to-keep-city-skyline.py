class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
            raw_max = []
            n = len(grid)

            for val in grid:
                raw_max.append(max(val))

            col_max = []
            ziped = list(zip(*grid))

            for val in ziped:
                col_max.append(max(val))
            
            mat = [[] for val in range(n)]

            for raw in range(n):
                for col in range(n):
                    mat[raw].append(min(raw_max[raw],col_max[col]))

            summ = 0

            for raw in range(n):
                for col in range(n):
                    summ += mat[raw][col] - grid[raw][col]
                    
            return summ 
        