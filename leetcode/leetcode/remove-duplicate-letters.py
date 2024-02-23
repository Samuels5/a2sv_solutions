class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []

        for val in s:
            while stack and stack[-1] > val and val not in stack and count[stack[-1]]:
                poped = stack.pop()
                
            count[val] -= 1
            if val not in stack:
                stack.append(val)



        return ''.join(stack)