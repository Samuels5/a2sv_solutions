class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stack = []
        ans = []
        size = len(nums)

        def back(idx):
            s = sorted(stack)
            if s not in ans:
                ans.append(s)
            for i in range(idx,size):
                stack.append(nums[i])
                back(i+1)
                stack.pop()
        back(0)
        return ans
            

        