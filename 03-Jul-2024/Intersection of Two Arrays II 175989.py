# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=Counter(nums1)
        d=Counter(nums2)
        a=[]
        for num in d.keys():
            if num in c:
                a.extend([num]*min((c[num],d[num])))
                
        return a