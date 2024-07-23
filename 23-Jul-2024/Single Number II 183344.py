# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        
        
        for val in nums:
            one = (one^val)&(~two)
            two = (two^val)&(~one)
            
        return one