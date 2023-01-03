t=int(input())
while(t!=0):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    x=0
    for i in range(0,a):
        x=max(x,sum(arr[i:i+b]))
    print(x)
    t=t-1
