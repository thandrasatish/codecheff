t=int(input())
l=[]
for i in range(t):
    l=list(map(int,input().split()))
    print(max(l),l[0]+l[1],sep=' ')
