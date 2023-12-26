class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right = 0
        res = 0
        for i, a in enumerate(flips, 1):
            right = max(right, a)
            if right == i:
                res += 1
        return res

        