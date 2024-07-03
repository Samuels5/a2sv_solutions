# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n > 3:
            min_diff = float("inf")
            nums = sorted(nums)
            window = (n-1)-3
            for i in range(n):
                if i+window >= n:
                    break
                else:
                    min_diff = min(nums[i+window]-nums[i], min_diff)
                    
            return min_diff
        
        return 0
        