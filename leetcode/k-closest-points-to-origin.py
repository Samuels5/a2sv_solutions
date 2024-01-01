class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            distances.append((point, distance))
        distances.sort(key=lambda x: x[1])
        result = []
        for i in range(k):
            result.append(distances[i][0])
        return result