class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count=0
        x=points[0][0]
        y=points[0][1]
        for i in range(len(points)-1):
            count+=max(abs(x-points[i+1][0]),abs(y-points[i+1][1]))
            x=points[i+1][0]
            y=points[i+1][1]
        return count