class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def cal(weights,capacity,days):
            sumi = 0
            count = 1
            r = 0
            for val in weights:
                sumi+=val
                if sumi>capacity:
                    sumi = val
                    count += 1
                if count > days:
                    return False
            return True

        left = max(weights)
        right = sum(weights)
        if cal(weights,left,days):
            return left
        while left <= right:
            mid = (left + right)//2
            
            if cal(weights,mid,days):
                right = mid
            else:
                left = mid
            
            if left +1 == right:
                return right   
