# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        count = defaultdict(int)
        for fr, to in edges:
            d[fr].append(to)
            count[to]+=1
        ans = [set() for i in range(n)]
        q = deque()#idx,[]
        for i in range(n):
            if not count[i]:
                q.append((i))
                
        while q:
            idx = q.popleft()
            for dir in d[idx]:
                count[dir]-=1
                ans[dir].update(ans[idx])
                ans[dir].add(idx)
                if not count[dir]:
                    q.append((dir))
        
        return [sorted(list(set(val))) for val in ans]