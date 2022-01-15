for i in range(int(input())):
    a,b=map(int,input().split())
    if(a>0 and a<=1000):
        print(float(a*b))
    elif(a>1000):
        print(float((a*b)-(a*b*0.10)))
