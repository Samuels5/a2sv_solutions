class Solution:
    def bestClosingTime(self, customers: str) -> int:
        li = []

        for val in customers:
            if val == 'Y':
                li.append(1)
            else:
                li.append(0)
        total = 0
        li2 = [sum(li)]
        sumi = sum(li)
        for idx,val in enumerate(li):
            if val == 1:
                sumi-=1
            else:
                sumi += 1
            li2.append(sumi)
        mini = min(li2)

        return li2.index(mini)



        