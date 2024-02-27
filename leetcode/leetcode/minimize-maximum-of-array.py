class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sumi = 0
        
        for idx,val in enumerate(nums):
            sumi += val
            average = (sumi + idx)//(idx+1)
            maxi = max(average,maxi)

        return maxi



        