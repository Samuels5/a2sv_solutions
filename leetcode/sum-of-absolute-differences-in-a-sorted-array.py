class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sm,n=0,len(nums)
        lst=[]
        tot=sum(nums)
        for i in range(n):
            sm+=nums[i]
            x=((i+1)*nums[i]-sm)+(tot-sm-(n-i-1)*nums[i])
            lst.append(x)
        return lst