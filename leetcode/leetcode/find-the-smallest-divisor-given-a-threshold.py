class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def cal(nums,div,threshold):
            count = 0
            for val in nums:
                count += (val+div-1)//div
            if count <= threshold:
                return True
            else:
                return False
        left = 0
        right = max(nums)+1
        while left + 1 < right:
            mid = (left+right)//2
            if cal(nums,mid,threshold):
                right = mid
            else:
                left = mid

        return right
