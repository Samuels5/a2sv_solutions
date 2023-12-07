class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        re=[]
        while j<len(nums):
            re.append(nums[i])
            re.append(nums[j])
            i+=1
            j+=1
        return re

        