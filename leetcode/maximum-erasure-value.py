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

                




















        # seen=set()
        # res=0
        # i=0
        # tot=0
        # for j in range(len(nums)):
        #     x=nums[j]
        #     while i < j and x in seen: 
        #         seen.remove(nums[i])
        #         tot-=nums[i]
        #         i+=1                        
        #     tot+=x
        #     seen.add(x)
        #     res=max(res, tot)            
        # return res



















