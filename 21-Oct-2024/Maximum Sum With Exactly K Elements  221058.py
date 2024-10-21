# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num = max(nums)
        maxi = 0
        for i in range(k):
            maxi += num
            num +=  1

        return maxi
