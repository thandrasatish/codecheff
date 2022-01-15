req,bal=input().split()
req=float(req)
bal=float(bal)
if req%5==0 and req<=bal-0.5:
    print(bal-0.5-req)
else:
    print(bal)
