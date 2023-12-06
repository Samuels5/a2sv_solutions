class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        re=[]
        while j<len(nums):
            re.extend([nums[j]]*nums[i])
            i+=2
            j+=2
        new=[]
        return re