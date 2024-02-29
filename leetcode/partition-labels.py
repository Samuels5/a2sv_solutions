class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = 0
        res = []
        
        for mid in range(len(s)):
            right = max(right, s.rfind(s[mid]))
            if mid == right:
                res.append(right-left+1)
                left = right + 1

        return res