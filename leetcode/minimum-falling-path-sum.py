class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ans = float('inf')

        dp = [[float('inf') for _ in range(c)] for _ in range(r)]

        for i in range(c):
            ans = min(ans, self.rec(0, i, matrix, dp))

        return ans

    def rec(self, i, j, arr, dp):
        if i == len(arr):
            return 0
        if j < 0 or j >= len(arr[0]):
            return float('inf')

        if dp[i][j] != float('inf'):
            return dp[i][j]

        ops1 = self.rec(i + 1, j - 1, arr, dp)
        ops2 = self.rec(i + 1, j, arr, dp)
        ops3 = self.rec(i + 1, j + 1, arr, dp)

        dp[i][j] = arr[i][j] + min(ops1, min(ops2, ops3))
        return dp[i][j]