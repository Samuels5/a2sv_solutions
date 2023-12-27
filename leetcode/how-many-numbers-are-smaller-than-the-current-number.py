class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num1=nums.copy()
        nums.sort()
        n=[]
        for i in num1:
            j=nums.index(i)
            n.append(j)
        return n



