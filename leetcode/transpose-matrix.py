class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        grid=[[] for i in range(len(matrix[0]))]
        for raw in range(len(matrix)):
            for col in range(len(matrix[0])):
                grid[col].append(matrix[raw][col])
        return grid
        