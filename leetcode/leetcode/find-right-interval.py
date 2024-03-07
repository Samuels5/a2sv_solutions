class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [s for s,e in intervals]
        de = {s:i for i,s in enumerate(start)}
        ans = []
        start.sort()
        # print(start)
        for st,end in intervals:
            # print(st,end)
            num = bisect_left(start,end)
            if num<len(start):
                ans.append(de[start[num]])
            else:
                ans.append(-1)
        return ans
            




        