class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        ans = []
        size = len(candidates)
        self.target = target

        def back():
            sumi = sum(stack)
            if sumi > self.target:
                return
            if sumi == self.target:
                s = sorted(stack)
                if s not in ans:
                    ans.append(s)
            for i in range(size):
                stack.append(candidates[i])
                back()
                stack.pop()
        back()
        return ans