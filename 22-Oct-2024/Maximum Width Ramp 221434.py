# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [(nums[0],0)]
        for idx,val in enumerate(nums[1:]):
            if stack[-1][0] > val:
                stack.append((val,idx+1))
                
        maxi = -float('inf')
        for idx in range(len(nums)-1,-1,-1):
            while stack and stack[-1][0] <= nums[idx]:
                maxi = max(maxi,idx - stack.pop()[1])

        return maxi
