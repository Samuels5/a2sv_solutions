class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini = min(nums)
        count = 0
        for idx, val in enumerate(nums):
            dif = target - val
            bd = bisect_right(nums,dif)
            if bd > idx:
                count += 2**(bd-idx-1)

        return count%(10**9 + 7)