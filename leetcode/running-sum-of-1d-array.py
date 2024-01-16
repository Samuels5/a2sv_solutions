class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        sumi=0
        for val in nums:
            sumi+=val
            arr.append(sumi)
        return arr
