class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono = []
        d = {num:i for i,num in enumerate(nums1)}
        ans = [-1] * len(nums1)
        for val in nums2:
            while mono and mono[-1] < val:
                poped = mono.pop()
                if poped in d:
                    ans[d[poped]] = val
                
            mono.append(val)

        return ans