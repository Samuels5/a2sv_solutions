class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count = 1
        val = points[0][1]
        for idx in range(len(points)-1):
            print(points[idx])
            if points[idx+1][0] <= val and val <= points[idx+1][1]:
                continue
            else:
                count += 1 
                val = points[idx+1][1]
                
        return count
