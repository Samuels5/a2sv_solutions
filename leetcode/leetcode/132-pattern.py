class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        pre = []
        num = inf

        for idx,val in enumerate(nums):
            num = min(num,val)
            while stack and nums[stack[-1][0]]<=val:
                poped = stack.pop()
            stack.append((idx,num))

            if len(stack)>1:
                if val >stack[-1][1] and val >stack[-2][1]:
                    return True

        return False

        