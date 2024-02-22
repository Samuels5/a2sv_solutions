class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for i,val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                poped = stack.pop()
                ans[poped[0]] = i-poped[0]
                
            stack.append((i,val))
        return ans
        