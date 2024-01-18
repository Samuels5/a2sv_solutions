class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')
        zero = 0
        score = 0
        for i in range(1, len(s)):
            if s[i-1] == '0':
                zero += 1
            if s[i-1] == '1':
                one -= 1
            score = max(score, zero + one)
        return score