t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))
    if(n%2==1):
        print("NO")
    else:
        x=False
        l.sort()
        for i in range(0,n,2):
            if(l[i]!=l[i+1]):
                print("NO")
                x=True
                break
        if(x==False):
            print("YES")
    t=t-1
