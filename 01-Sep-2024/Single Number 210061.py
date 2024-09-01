# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key, val in count.items():
            if val == 1:
                return key