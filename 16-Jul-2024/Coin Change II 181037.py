# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        arr = [0 for i in range(amount+1)]
        arr[0] = 1
        
        for val in coins:
            for num in range(1,len(arr)):
                if num-val>=0:
                    arr[num] += arr[num-val]
                    
        return arr[-1]