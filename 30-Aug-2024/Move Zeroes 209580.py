# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right, val in enumerate(nums):
            if val != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
