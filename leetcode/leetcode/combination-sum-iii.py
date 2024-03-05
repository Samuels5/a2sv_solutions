class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        stack = []
        ans = []

        def back(idx):
            if len(stack)>k:
                return 
            sumi = sum(stack)
            s = sorted(stack)
            
            if sumi == n and len(stack)==k and s not in ans:
                ans.append(s)
            for i in range(idx,len(nums)):
                stack.append(nums[i])
                back(i+1)
                stack.pop()
        back(0)
        return ans
            

        