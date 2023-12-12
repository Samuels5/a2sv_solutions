class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d=defaultdict(int)
        for i in arr:
            d[i]+=1
            if d[i]>0.25*len(arr):
                return i