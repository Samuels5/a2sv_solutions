class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal(piles,h,val):
            count = 0
            for num in piles:
                count += (num+val-1)//val
            return True if count <= h else False
        # print(cal(piles,h,5))

        left = 0
        right = sum(piles)
        
        while left <= right:
            mid = (left + right)//2
            
            if cal(piles,h,mid):
                right = mid
            else:
                left = mid
            
            if left +1 == right:
                return right  