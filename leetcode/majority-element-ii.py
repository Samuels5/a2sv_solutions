class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=set([])
        for num in nums:
            if nums.count(num)>len(nums)/3:
                x.add(num)
        return list(x)
        