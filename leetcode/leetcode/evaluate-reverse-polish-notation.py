class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val in '+-/*':
                b = stack.pop()
                a = stack.pop()
                if val == '+':
                    stack.append(a+b)
                elif val == '-':
                    stack.append(a-b)
                elif val == '/':
                    stack.append(int(a/b))
                else:
                    stack.append(a*b)
            else:
                stack.append(int(val))
                
        return stack.pop()
