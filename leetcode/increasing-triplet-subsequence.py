class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1=float('inf')
        min2=float('inf')
        i=0
        while i<len(nums):
            if nums[i]>min2:
                return True
            if nums[i]<min1:
                min1=nums[i]
            elif nums[i]>min1:
                min2=nums[i]
            i+=1
        return False
        