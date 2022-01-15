a=int(input())
for i in range(a):
    b=int(input())
    arr = [int(x) for x in input().split()]
    if(sum(arr)%2==0):
        print(1)
    else:
        print(2)
       
