class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        i=0
        j=sum(nums)
        d={0:j}
        while i<len(nums):
            if nums[i]==0:
                j+=1
                d[i+1]=j
            else:
                j-=1
                d[i+1]=j
            i+=1
        maxi=max(d.values())
        re=[]
        for idx,val in d.items():
            if val==maxi:
                re.append(idx)
        return re