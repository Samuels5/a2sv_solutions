class Solution:
    def smallestNumber(self, num: int) -> int:
        nums=list(str(num))
        nums.sort()
        if nums[0]=='0':
            idx0=len(nums) - nums[::-1].index('0')-1
            if idx0==len(nums)-1:
                return 0

            nums[0],nums[idx0+1]=nums[idx0+1],nums[0]
            return int(''.join(nums))

        if nums[0] in '123456789':
            return int(''.join(nums))
        
        if nums[0] == '-':
            nums=nums[1:]
            nums.sort(reverse=True)
            return -int(''.join(nums))
        
        