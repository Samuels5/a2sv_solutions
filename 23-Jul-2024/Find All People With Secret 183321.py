# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        times = dict()
        known = set([firstPerson,0])
        
        for x,y,time in meetings:
            ad = times.setdefault(time, dict())
            ad.setdefault(x, []).append(y)
            ad.setdefault(y, []).append(x)

        def DFS(node, graph, visited, comp):
            visited[node] = True 
            comp.add(node)
            for child in graph[node]:
                if not visited[child]:
                    comp.add(child)
                    DFS(child, graph, visited, comp)
            
        for time in sorted(times.keys()):
            graph = times[time]

            visited = dict(zip(graph.keys(), [False]*len(graph.keys())))
            it = iter(graph.keys())
            components = []

            for node in it:
                if visited[node]:
                    continue
                c = set()
                DFS(node, graph, visited, c)
                components.append(c)

            for c in components:
                if len(known.intersection(c)) > 0:
                    known.update(c)

        return known