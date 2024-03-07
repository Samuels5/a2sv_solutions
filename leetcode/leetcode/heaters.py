class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = []
        for val in houses:
            arr = []
            num = bisect_left(heaters,val)
            num1 = bisect_right(heaters,val)
            if num != 0 and val in heaters:
                arr.append(abs(val - heaters[num]))
            elif num != 0 and val not in heaters:
                arr.append(abs(val - heaters[num-1]))
            else:
                arr.append(abs(val - heaters[0]))
            if num1 == len(heaters):
                num1-=1
            arr.append(abs(val-heaters[num1]))
            ans.append(min(arr))
            
        return max(ans)
        