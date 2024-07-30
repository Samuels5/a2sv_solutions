# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        smallest = arr[-1]
        left = -1

        for i in range(len(arr)-2, -1, -1):
            if arr[i] > smallest:
                left = i
                break
            smallest = min(arr[i], smallest)

        if left == -1:
            return arr
        right = left + 1

        for i in range(left + 2, len(arr)):
            if arr[i] < arr[left] and arr[i] > arr[right]:
                right = i

        l = arr[left]
        arr[left] = arr[right]
        arr[right] = l
        
        return arr