# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        st = set(t)
        l = 0
        ans = ''
        for r in range(len(s)):
            if s[r] in st:
                count[s[r]] -= 1
            flag = True
            while flag:
                # print(count, flag)
                for key, val in count.items():
                    if val > 0:
                        flag = False
                        break
                else:
                    temp = s[l:r+1]
                    # print(temp)
                    if len(temp)<len(ans) or ans == '':
                        ans = temp
                    # if l>len(s)-1:
                    #     break
                    if s[l] in st:
                        count[s[l]] += 1
                    l += 1

        return ans
        