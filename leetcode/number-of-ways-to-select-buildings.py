class Solution:
    def numberOfWays(self, s: str) -> int:
        li1 = []
        count = 0
        
        for val in s:
            if val == '0':
                count += 1
                li1.append(0)
            else:
                li1.append(count)
        num = 0
        pre = []

        for val in li1:
            num += val
            pre.append(num)
        total = 0

        for idx,val in enumerate(s):
            if val == '0':
                total += pre[idx]
        li2 = []
        count1 = 0

        for val in s:
            if val == '1':
                count1 += 1
                li2.append(0)
            else:
                li2.append(count1)
        num = 0
        pre1 = []
        for val in li2:
            num += val
            pre1.append(num)

        for idx,val in enumerate(s):
            if val == '1':
                total += pre1[idx]

        return total

        


                

        