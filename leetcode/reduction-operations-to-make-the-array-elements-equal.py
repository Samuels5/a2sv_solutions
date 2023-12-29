class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        arr=[]
        for val in c.items():
            arr.append(val[0])
        arr.sort()
        count=0
        for idx,val in enumerate(arr):
            count+=idx*c[val]
        return count
        