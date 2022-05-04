for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    maxi=max(l)
    count=0
    for i in range(n):
        while l[i]>0:
            l[i]=l[i]-x
            count+=1
    print(min(maxi,count))
