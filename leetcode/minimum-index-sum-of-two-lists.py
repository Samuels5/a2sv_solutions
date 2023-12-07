class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        re=[]
        for i in list1:
            if i in list2:
                re.append(i)
        l=0
        d={}
        for j in re:
            d[j]=list1.index(j) + list2.index(j)
        low=min(d.values())
        l=[]
        for i,j in d.items():
            if j==low:
                l.append(i)
        return l
