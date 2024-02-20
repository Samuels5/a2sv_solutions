class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        count = 0
        for idx,val in enumerate(nums):
            count = max(count,val)
            print(count)
            if idx!=len(nums)-1 and count == 0:
                return False
            count -= 1
        return True

        