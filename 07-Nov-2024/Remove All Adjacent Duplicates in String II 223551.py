# Problem: Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for val in s:
            if not stack or stack[-1][0] != val:
                stack.append([val,k-1])
            else:
                v = stack.pop()
                if v[1] - 1 > 0:
                    stack.append([v[0],v[1]-1])
        res = []
        for val in stack:
            for i in range(k - val[1]):
                res.append(val[0])
        # print(res)
        return ''.join(res)