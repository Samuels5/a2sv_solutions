# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for fr, to in edges:
            d[fr].append(to)
        d2 = defaultdict(set)
        for i in range(n):
            q = deque()
            q.append(i)
            while q:
                num = q.popleft()
                for val in d[num]:
                    if i not in d2[val]:
                        d2[val].add(i)
                        q.append(val)
        # print(d2)
        ans = []
        for i in range(n):
            ans.append(sorted(list(d2[i])))

        return ans

