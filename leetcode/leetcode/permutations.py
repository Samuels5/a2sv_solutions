class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        ans = []
        size = len(nums)
        def back():
            
            for idx in range(size):
                if len(stack) == size:
                    if stack not in ans:
                        ans.append(stack[:])
                    continue
                if nums[idx] not in stack:
                    stack.append(nums[idx])
                    back()
                    stack.pop()
        back()
        return ans

        
          

        