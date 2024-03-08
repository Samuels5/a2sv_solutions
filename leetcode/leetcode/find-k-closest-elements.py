class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr1 = []
        for idx,val in enumerate(arr):
            # print(abs(val-x))
            arr1.append((idx,val,abs(val-x)))
        arr1.sort(key = lambda x: x[2])
        li = []
        for val in range(k):
            li.append(arr1[val][1])

        return sorted(li)
