# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float('inf')]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 0

        for fr, to, w in edges:
            dp[fr][to] = dp[to][fr] = w

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dp[j][k] > dp[i][k] + dp[i][j]:
                        dp[j][k] = dp[i][k] + dp[i][j]
                        
        num = float('inf')
        main = float('inf')
        for i in range(n-1,-1,-1):
            count = 0
            for val in dp[i]:
                if val <= distanceThreshold:
                    count += 1
                    
            if main > count:
                main = count
                num = i

        return num