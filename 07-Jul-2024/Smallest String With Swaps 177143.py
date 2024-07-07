# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [[i] for i in range(n)]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if len(self.rank[x]) < len(self.rank[y]):
                self.parent[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.parent[y] = x
                self.rank[x] += self.rank[y]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = UnionFind(len(s))
        for st, ed in pairs:
            dsu.union(st,ed)
        par = [sorted([s[num]for num in val],reverse = True) for val in dsu.rank]
        ans = []
        
        for num in range(len(s)):
            ans.append(par[dsu.find(num)].pop())

        return ''.join(ans)