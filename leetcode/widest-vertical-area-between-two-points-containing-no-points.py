class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        maxi=0
        for val in range(1,len(points)):
            width = points[val][0] - points[val-1][0]
            maxi=max(maxi, width)
        return maxi
        
        