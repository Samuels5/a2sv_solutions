class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        re=0
        for num in range(len(nums)+1):
            if num not in nums:
                re = num
        return re
                