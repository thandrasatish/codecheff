import math
l=[]
for i in range(int(input())):
    l=list(map(int,input().split()))
    r=math.gcd(l[0],l[1])
    p=l[0]*l[1]//r
    print(r,p,sep=' ')
    
    
