class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        dic =  {0:1}
        ans = 0

        for i in range(len(nums)):
            pref += nums[i]
            need = pref - goal
            ans += dic.get(need, 0)
            dic[pref] = dic.get(pref, 0) + 1

        return ans