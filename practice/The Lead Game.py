t=int(input())
lead=0
s1=0
s2=0
for i in range(t):
    p,q=map(int,input().split())
    s1=s1+ p 
    s2=s2+ q 
    if(s1>s2 and s1-s2>lead):
        lead=s1-s2
        leader=1 
    elif(s2>s1 and s2-s1>lead):
        leader=2 
        lead = s2-s1
print(leader,lead,sep=' ')
