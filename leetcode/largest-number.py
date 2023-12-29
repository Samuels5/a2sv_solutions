class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for num1 in range(len(nums)-1):
            for num in range(len(nums)-1):
                if str(nums[num])+str(nums[num+1])<str(nums[num+1])+str(nums[num]):
                    nums[num],nums[num+1] = nums[num+1],nums[num]
        if nums[0]== 0:
            return '0'
        return ''.join(map(str,nums))