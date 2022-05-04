import math
t = int(input())
for _ in range(t):
    n,m,x = map(int,input().split())
    sum = x*n
    if m==x:
        print(0)
    else:
        num = math.floor(sum/(x+1))    
        
        print(num)
