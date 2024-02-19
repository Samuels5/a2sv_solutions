class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = defaultdict(int)
        m = len(set(nums))
        n = len(nums)
        count = 0
        l = 0
        for i in range(len(nums)):
            d[nums[i]]+=1
            while len(d) == m:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            count += i - l + 1

        return n*(n+1)//2 - count






        return count

                

        