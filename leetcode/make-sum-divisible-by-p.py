class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s % p == 0: return 0 
   

        moddict = {}
        minv = float('inf')
        t = 0 

        moddict[0] = 0 
        cnt = 1
        for num in nums:
            t = (t + num) % p 
            if (t-s) % p in moddict:
                minv = min(minv, cnt - moddict[(t-s)%p])
            moddict[t] = cnt
            cnt += 1
            
        if minv == float('inf') or minv == len(nums):
            return -1
        else:
            return minv