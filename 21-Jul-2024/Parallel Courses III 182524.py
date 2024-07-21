# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = [0] * n
        can_take = [0] * n

        for pre, nex in relations:
            graph[pre - 1].append(nex - 1) 
            degree[nex - 1] += 1
        
        courses = [(0, x) for x in range(n) if degree[x] == 0]

        res = 0
        while courses:
            time_taken, course = courses.pop(-1)
            res = max(res, time_taken + time[course])
            for nex in graph[course]:
                degree[nex] -= 1
                can_take[nex] = max(can_take[nex], time_taken + time[course])
                if degree[nex] == 0:
                    courses.append((can_take[nex], nex))
        
        return res