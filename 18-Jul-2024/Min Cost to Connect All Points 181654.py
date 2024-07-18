# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                self.rank[y] += 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = UnionFind(n)

        def dis(a,b): 
            return abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1])

        edges = []
        
        for i in range(n):
            for j in range(n):
                edges.append((dis(i,j),i,j))

        edges.sort()
        res = 0

        for d, x, y in edges:
            if dsu.find(x) != dsu.find(y):
                dsu.union(x,y)
                res += d

        return res