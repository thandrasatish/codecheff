t=int(input())
while(t!=0):
    n=int(input())
    s=0
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
    while(n!=0):
        a,b=map(int,input().split())
        # s1=0
        if(a==1):
            s1=max(s1,b)
        # s2=0
        if(a==2):
            s2=max(s2,b)
        # s3=0
        if(a==3):
            s3=max(s3,b)
        # s4=0
        if(a==4):
            s4=max(s4,b)
        # s5=0
        if(a==5):
            s5=max(s5,b)
        # s6=0
        if(a==6):
            s6=max(s6,b)
        # s7=0
        if(a==7):
            s7=max(s7,b)
        # s8=0
        if(a==8):
            s8=max(s8,b)
        # print(s1+s2+s3+s4+s5+s6+s7+s8)
        n=n-1
    print(s1+s2+s3+s4+s5+s6+s7+s8)
    t=t-1
