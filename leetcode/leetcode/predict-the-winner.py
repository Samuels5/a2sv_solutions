class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        size = len(nums)
        def back(i, j):
            if i == j:
                return nums[i]
            leftDiff = nums[i] - back(i + 1, j)
            rightDiff = nums[j] - back(i, j - 1)
            return max(leftDiff, rightDiff)
        
        return back(0, size - 1) >= 0 