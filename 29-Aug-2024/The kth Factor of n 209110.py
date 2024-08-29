# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = []
        for num in range(1,n+1):
            if n%num == 0:
                arr.append(num)
        if k<=len(arr):
            return arr[k-1]
            
        return -1