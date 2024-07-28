# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        l=0
        count1 = 0
        
        for r in range(len(nums)):
            d[nums[r]]+=1
            while len(d)>k and l<len(nums):
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1

            count1 += r-l+1

        count2 = 0
        l=0
        d =defaultdict(int)

        for r in range(len(nums)):
            d[nums[r]]+=1
            while len(d)>(k-1) and l<len(nums):
                d[nums[l]]-=1
                if d[nums[l]]==0:
                    del d[nums[l]]
                l+=1
            count2 += r-l+1

        return count1-count2