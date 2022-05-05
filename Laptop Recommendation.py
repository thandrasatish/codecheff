from collections import Counter
t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=Counter(l)
    l1=[]
    for i,j in x.items():
        l1.append(j)
    p=max(l1)
    l2=[]
    for i,j in x.items():
        if(j==p):
            l2.append(i)
    if(len(l2)==1):
        print(l2[0])
    else:
        print("CONFUSED")
    t=t-1
    
