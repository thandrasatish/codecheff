t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    co1,co0 = 0,0
    ans = 0
    for j in range(n):
        if(l[j]==0):
            co0 += 1
        else:
            co1 += 1
    if(co1>=co0):
        print(1)
    else:
        print(0)



