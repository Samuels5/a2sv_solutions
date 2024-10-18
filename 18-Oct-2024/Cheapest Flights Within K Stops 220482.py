# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = {node: float('inf') for node in range(n)}
        distances[src] = 0
        processed = set()
        graph = defaultdict(list)
        for fr, to , pri in flights:
            graph[fr].append((to,pri))

        heap = [(0, src)]
        while heap and k >= 0:
            k-=1
            new = []
            for i in range(len(heap)):
                cost, curr = heapq.heappop(heap)
                # if curr in processed:
                #     continue
                # processed.add(curr)
                
                for child, weight in graph[curr]:
                    distance = cost + weight
                    if distance < distances[child]:
                        distances[child] = distance
                        new.append((distance, child))
            for val in new:
                heappush(heap, val) 
            # print(heap)
        # print(distances)
        return distances[dst] if distances[dst] != float('inf') else -1