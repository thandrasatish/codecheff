t=int(input())
while(t!=0):
    l=list(map(int,input().split()))
    s=input()
    s=list(s)
    x="abcdefghijklmnopqrstuvxywz"
    x=list(x)
    sum=0
    for i in range(len(x)):
        if(x[i] not in s):
            sum=sum + l[ord(x[i])-ord('a')]
    print(sum)
    t=t-1
