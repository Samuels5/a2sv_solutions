class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for num in range(len(nums)):
            for num2 in range(num+1,len(nums)):
                if nums[num]==nums[num2] and (num*num2)%k==0:
                    count+=1
        return count
