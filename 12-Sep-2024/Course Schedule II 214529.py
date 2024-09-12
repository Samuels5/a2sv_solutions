# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        s = set()
        d = defaultdict(list)
        count = Counter()
        for nd, de in prerequisites:
            d[nd].append(de) 
            count[de] += 1
        def dfs(num):
            ans.append(num)
            s.add(num)
            for val in d[num]:
                count[val] -= 1
                if count[val] == 0:
                    dfs(val)
        for num in range(numCourses):
            if num not in s and count[num] == 0:
                dfs(num)
        return ans[::-1] if len(s) == numCourses else []