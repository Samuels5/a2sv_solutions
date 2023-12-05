class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        j=0
        a=[0]
        while j<=len(nums) and i<len(nums):
            if j==len(nums) and nums[i]==1:
                a.append(j-i)
                break
            if nums[i]==1:
                if nums[j]==1:
                    j+=1
                    continue
                else:

                    a.append(j-i)
                    i=j
                    j+=1
            else:
                i+=1
                j=i
        return max(a)