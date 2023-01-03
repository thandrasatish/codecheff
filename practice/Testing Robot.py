t=int(input())
while(t!=0):
    a,b=map(int,input().split())
    s=input()
    l=[]
    l.append(b)
    for i in range(len(s)):
        if(s[i]=='R'):
            b=b+1
        else:
            b=b-1
        l.append(b)
    print(len(set(l)))
    t=t-1
