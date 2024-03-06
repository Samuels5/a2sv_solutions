class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if nums[0]>target:
            return [-1,-1]
        
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left]<target:
                    left += 1
                if nums[right]>target:
                    right -= 1
            if nums[left] == target and nums[right] == target:
                return [left,right]
        if left == right and nums[left] != target:
            return [-1,-1]
        return [left,right]

        