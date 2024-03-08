from bisect import bisect_left,bisect_right
n = input()
li = list(map(int,input().split()))
li.sort()
for _ in range(int(input())):
    b = int(input())
    if b < li[0]:
        print(0)
    elif b > li[-1]:
        print(len(li))
    else:    
        val = bisect_right(li,b)
        print(val)