# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, n):
        self.count = n
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
            self.count -= 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = UnionFind(n+1)

        for val in roads:
            dsu.union(val[0],val[1])

        st = set()

        for num in range(1,n+1):
            if dsu.find(num) != dsu.find(1):
                st.add(num)

        mini = inf

        for val in roads:
            if val[0] not in st or val[1] not in st:
                mini = min(mini,val[2])
                
        return mini