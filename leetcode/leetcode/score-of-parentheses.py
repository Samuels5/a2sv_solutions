class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for val in s:
            if val == '(':
                stack.append('(')
            else:
                num = 0
                while stack[-1] != '(':
                    num += stack.pop()
                poped = stack.pop()
                stack.append(max(1,2*num))

        return sum(stack) 



        