class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in '({[':
                stack.append(val)
            elif val == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif val == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif val == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False