class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        i=0
        d={}
        while i<len(nums):
            d[nums[i]]=i
            i+=1
        for value,value1 in operations:
            index1=d[value]
            nums[index1]=value1
            del(d[value])
            d[value1]=index1

        return nums