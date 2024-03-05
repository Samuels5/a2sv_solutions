class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        ans = []
        poped = []
        size = len(candidates)
        def back(idx):
            if sum(stack)>target:
                return 
            s = sorted(stack)
            sumi = sum(s)
            if sumi == target and s not in ans:
                ans.append(s)
            # print(stack)
            for i in range(idx,size):
                if poped and poped[-1] == candidates[i]:
                    continue

                stack.append(candidates[i])
                back(i+1)
                poped.append(stack.pop())
        back(0)
        return ans