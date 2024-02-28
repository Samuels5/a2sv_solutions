class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        size = len(nums)

        for val in nums:
            nums.append(val)
            if val == maxi:
                break

        ans = [-1]*size
        stack = []

        for idx,val in enumerate(nums):
            while stack and stack[-1][1]<val:
                poped = stack.pop()
                if poped[0]<size:
                    ans[poped[0]] = val
            stack.append((idx,val))
            
        return ans