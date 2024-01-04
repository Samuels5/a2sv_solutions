class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        r=0
        l=0
        re=-1
        while r<len(nums1) and l<len(nums2):
            if nums1[r]==nums2[l]:
                re=nums1[r]
                break
            elif nums1[r]<nums2[l]:
                r+=1
            elif nums1[r]>nums2[l]:
                l+=1
        return re

        