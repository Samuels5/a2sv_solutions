# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        output = 0
        j = 0
        
        for i in range(len(s)):
            if g[j] <= s[i]: 
                j = j + 1
                output = output + 1
            if j == len(g):
                break
        
        return output