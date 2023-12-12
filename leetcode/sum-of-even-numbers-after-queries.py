class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        sumi=0
        for i in nums:
            if i%2==0:
                sumi+=i
        for value,index in queries:
            if nums[index]%2!=0 and value%2!=0:
                sumi+=nums[index]+value
            elif nums[index]%2==0 and value%2==0:
                sumi+=value
            elif nums[index]%2==0 and value%2!=0:
                sumi-=nums[index]
            nums[index] += value
            
            arr.append(sumi)
        return arr