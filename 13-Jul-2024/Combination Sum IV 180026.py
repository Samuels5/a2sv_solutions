# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(target):
            if target < 0:
                return 0
                
            if target == 0:
                return 1

            if target not in memo:
                num = 0
                for val in nums:
                    num += dp(target - val)
                memo[target] = num

            return memo[target]

        return dp(target)