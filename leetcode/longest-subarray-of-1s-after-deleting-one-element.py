class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums1=list(map(str,nums))
        st=''.join(nums1)
        st1=[]
        if '0' in st:
            st1=st.split('0')
        else:
            return len(st)-1
        maxi=0
        for num in range(len(st1)-1):
            if len(st1[num])+len(st1[num+1])>maxi:
                maxi=len(st1[num])+len(st1[num+1])
        return maxi


        

        