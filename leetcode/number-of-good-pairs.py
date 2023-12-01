class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    k+=1
        return k
