class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = { num : i for i, num in enumerate(arr2)}
        n = len(arr2)
        arr1.sort(key=lambda x: index[x] if x in index else n + x)
        return arr1
        