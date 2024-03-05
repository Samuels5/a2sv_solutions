class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = []
        ans = []

        def back(idx):
            if len(stack) >= k:
                ans.append(stack[:])
                return None

            for i in range(idx,n+1):
                stack.append(i)
                back(i+1)
                stack.pop()

        back(1)
        return ans
                

