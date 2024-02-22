class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        flag = 1
        re = 0
        for val, count in d.items():
            if count == 1 and flag:
                re += count
                flag -= 1
            elif count % 2 == 1:
                if flag:
                    re += count
                    flag -= 1
                else:
                    re += count - 1
            else:
                re += count
        return re
        