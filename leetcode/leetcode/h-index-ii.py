class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.reverse()
        ans = 0
        for idx,val in enumerate(citations):
            if val >= idx + 1:
                ans = idx + 1
        return ans
