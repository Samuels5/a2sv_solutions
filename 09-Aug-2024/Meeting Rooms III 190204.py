# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = []
        available = [i for i in range(n)]
        count = [0] * n
        meetings.sort()

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                
            else:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(busy, (end_time + end - start, room))
                
            count[room] += 1

        return count.index(max(count))