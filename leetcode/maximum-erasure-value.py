class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d=defaultdict(int)
        sumi=0
        l=0
        for r in range(len(nums)):
            d[nums[r]]+=1
            while d[nums[r]] > 1:
                d[nums[l]]-=1
                l+=1
            sumi=max(sumi,sum(nums[l:r+1]))
        return sumi



















