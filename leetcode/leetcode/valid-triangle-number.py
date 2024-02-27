class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        count = 0
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n-1
            while left < right:
                summ = nums[left] + nums[right]

                if summ > nums[i]:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
