class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = [0] * (len(nums)+1)
        for start, stop in requests:
            n[start] += 1
            n[stop+1] -= 1
        
        n = list(accumulate(n))
        n.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for freq, num in zip(n, nums):
            res += num * freq
        return res % 1_000_000_007