class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def cal(s,right,left):
            if len(s) == 2*n:
                ans.append(s)
            if left < n:
                cal(s+'(', right, left+1)

            if right < left:
                cal(s+')', right+1, left)
        
        cal('',0,0)
        
        return ans
            
        