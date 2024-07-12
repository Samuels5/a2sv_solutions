# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        nums.sort()
        maxi = -float('inf')

        for i in range(len(nums)-1):
            maxi = max(nums[i+1]-nums[i], maxi)
        
        return maxi
