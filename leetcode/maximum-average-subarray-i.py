class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=sum(nums[:k])
        maxi=sumi
        
        for num in range(k,len(nums)):
            sumi+=nums[num]
            sumi-=nums[num-k]
            maxi=max(maxi,sumi)
            
            
        return maxi/k

        