class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def cal(s):
            for val in s:
                if val.lower() not in s or val.upper() not in s:
                    return False
            return True
        ans = []
        for left in range(len(s)):
            for right in range(left,len(s)+1):
                if cal(s[left:right]):
                    ans.append(s[left:right])
        ans.sort(key = lambda x: len(x), reverse = True)
        
        return ans[0]


