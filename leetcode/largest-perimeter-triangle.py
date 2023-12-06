class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for num in range(len(nums)-1,1,-1):
          
          if nums[num]<nums[num-1]+nums[num-2]:
            return sum([nums[num],nums[num-1],nums[num-2]])
        return 0
          