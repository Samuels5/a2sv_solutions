class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        ans = []
        size =  len(nums)
        def back(idx):
            ans.append(stack[:])
            for idx in range(idx,size):
                stack.append(nums[idx])
                back(idx+1)
                stack.pop()
        back(0)
        return ans
