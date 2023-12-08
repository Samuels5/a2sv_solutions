class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s=set([])
        for rang in ranges:
            for i in range(rang[0],rang[1]+1):
                s.add(i)
        for j in range(left,right+1):
            if j not in s:
                return False
        return True

        