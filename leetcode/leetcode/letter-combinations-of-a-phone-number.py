class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stack = []
        ans = []
        de = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        size = len(digits)
        if not digits:
            return []
        def back(idx):
            # print(stack)
            if len(stack) == size:
                ans.append(''.join(stack))
                return None
            for i in range(idx,size):
                for j in de[digits[i]]:
                    stack.append(j)
                    back(i + 1)
                    stack.pop()
                
        back(0)
        return ans


        