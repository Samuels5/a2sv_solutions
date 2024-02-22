class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        print(paths)
        for val in paths:
            if stack and val == '..' :
                stack.pop()
            elif val not in ['','.','/','..']:
                stack.append(val)
        return '/' + '/'.join(stack)

        