def satish(n,l):
    l.sort()
    for i in range(1,n-1):
        if((l[i]-l[i-1])==2*(l[i+1]-l[i]) or (2*(l[i]-l[i-1])==l[i+1]-l[i])):
            pass
        else:
            return "NO"
    return "YES"

t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(satish(n,l))
    t=t-1
        
# Bi−Bi−1=2⋅(Bi+1−Bi), or
# 2⋅(Bi−Bi−1)=Bi+1−Bi
