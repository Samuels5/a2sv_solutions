class Solution:
    def minimumSteps(self, s: str) -> int:
        total = 0
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                count+=1
            else:
                total += count
        return total
         
        