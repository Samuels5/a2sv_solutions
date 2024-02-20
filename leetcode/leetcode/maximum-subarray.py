class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        mini =0
        maxi = float('-inf')
        for val in nums:
            pre += val
            maxi = max(maxi,pre-mini)
            mini = min(mini,pre)

        # print(li)
        
        if len(nums)<2:
            return nums[0]
        # print(maxi,mini)
        
        return maxi
        