t=int(input())
while(t!=0):
    n=int(input())
    l=list(map(int,input().split()))
    print(len(set(l)))
    t=t-1
