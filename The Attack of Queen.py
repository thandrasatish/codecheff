
z=int(input())
while(z):
    n,x,y=map(int,input().split())
    p=n-x+x-1+n-y+y-1
    q=min(x-1,y-1)
    r=min(x-1,n-y)
    s=min(n-x,y-1)
    t=min(n-x,n-y)
    print(p+q+r+s+t)
    z=z-1
