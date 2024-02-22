class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        li = list(s)
        for val in li:
            if val == '*' and stack:
                stack.pop()
            else:
                stack.append(val)
        return ''.join(stack)
        