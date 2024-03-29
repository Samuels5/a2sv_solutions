class NumArray:

    def __init__(self, nums: List[int]):
        self.arr=[]
        self.nums=nums
        self.pre=[]
        sumi=0
        for val in nums:
            sumi+=val
            self.pre.append(sumi)
        print(self.pre)
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.pre[right] 
        return self.pre[right] - self.pre[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)