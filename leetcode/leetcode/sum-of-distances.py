class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sumi = defaultdict(int)
        count = defaultdict(int)
        li = []
        for idx, val in enumerate(nums):
            li.append(count[val]*idx -sumi[val])
            count[val]+=1
            sumi[val]+=idx
        sumi = defaultdict(int)
        count = defaultdict(int)
        for idx in range(len(nums)-1,-1,-1):
            li[idx]+=sumi[nums[idx]]-count[nums[idx]]*idx
            count[nums[idx]]+=1
            sumi[nums[idx]]+=idx

        return li
        