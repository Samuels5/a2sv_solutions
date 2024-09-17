# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        for word in words:
            pat = defaultdict(str)
            d = defaultdict(str)
            flag = 0
            
            for idx, val in enumerate(word):
                if val in pat :
                    if not pat[val] == pattern[idx] :
                        flag = 1
                        break
                elif pattern[idx] in d:
                    if not d[pattern[idx]] == val :
                        flag = 1
                        break
                else:
                    pat[val] = pattern[idx]
                    d[pattern[idx]] = val

            if not flag:
                ans.append(word)

        return ans