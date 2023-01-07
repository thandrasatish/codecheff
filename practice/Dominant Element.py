from collections import Counter
t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))
    x=Counter(l)
    l1=[]
    for i,j in x.items():
        l1.append(j)
    x1=max(l1)
    l1.remove(x1)
    if(x1 not in l1):
        print("YES")
    else:
        print("NO")
    t=t-1
