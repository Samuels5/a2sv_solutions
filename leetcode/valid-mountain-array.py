class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_num = max(arr)
        if max_num == arr[len(arr) - 1] or max_num == arr[0]:
            return False
        max_found = False
        for i in range(len(arr) - 1):
            if arr[i] == max_num:
                max_found = True
            if max_found and arr[i] <= arr[i + 1]:
                return False
            elif not max_found and arr[i] >= arr[i + 1]:
                return False
        return True
        