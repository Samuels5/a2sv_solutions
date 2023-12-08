class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        grater=[]
        equal=[]
        for num in nums:
            if num>pivot:
                grater.append(num)
            elif num==pivot:
                equal.append(num)
            elif num<=pivot:
                less.append(num)
        re=[]
        re+=less+equal+grater
        return re