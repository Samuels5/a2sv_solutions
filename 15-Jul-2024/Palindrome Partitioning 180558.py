# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        stack = []
        def isPalandrom(s,idx,j):
            while idx<j:
                if s[idx] != s[j]:
                    return False
                idx += 1
                j -= 1
                
            return True 

        def back(idx):
            if idx >= len(s):
                ans.append(stack.copy())
                return 

            for j in range(idx, len(s)):
                if isPalandrom(s, idx, j):
                    stack.append(s[idx:j+1])
                    print(stack)
                    back(j + 1)
                    stack.pop()
        back(0)

        return ans