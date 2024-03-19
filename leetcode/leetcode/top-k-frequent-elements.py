class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        for key, val in count.items():
            arr.append([key,val])
        arr.sort(key = lambda x: x[1], reverse = True)
        li = []
        for val in range(k):
            li.append(arr[val][0])
        return li
        