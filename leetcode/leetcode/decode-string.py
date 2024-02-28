class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        size = len(s)

        for val in s: 
            if val.isnumeric():
                if stack and stack[-1].isnumeric():
                    stack[-1]+=val
                else:
                    stack.append(val)
            elif val == ']':
                li = []
                while stack and stack[-1] != '[':
                    li.append(stack.pop())
                stack.pop()
                n = stack.pop()
                stack.append(''.join(li[::-1])*int(n))
            else:
                stack.append(val)

        return ''.join(stack)

        