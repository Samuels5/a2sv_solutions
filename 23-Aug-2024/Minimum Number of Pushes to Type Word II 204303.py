# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        d = defaultdict(int)

        for val in word:
            d[val] += 1
        arr = []

        for val, num in d.items():
            arr.append((val,num))

        arr.sort(key=lambda x: x[1], reverse=True)
        new = [[] for i in range(8)]
        i = 0
        for val in arr:
            new[i].append(val[0])
            i+= 1
            if i == 8:
                i=0
        count = 0
        for val in new:
            for idx,v in enumerate(val):
                count += (idx+1)*d[v]
                
        return count





