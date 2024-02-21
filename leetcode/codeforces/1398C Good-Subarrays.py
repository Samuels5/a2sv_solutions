tests = int(input())
from collections import defaultdict
for t in range(tests):
    n = int(input())
    st = list(map(int,list(input())))
    sumi = 0
    pre = [0]
    d = defaultdict(int)
    for num in st:
        sumi += num
        pre.append(sumi)
        
    ans = 0
    for idx, val in enumerate(pre):
        dif = val - idx -1
        if dif in d:
            ans += d[dif]
        d[dif] += 1
    
    print(ans)