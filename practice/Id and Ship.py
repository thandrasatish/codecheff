t=int(input())
for i in range(t):
    arr=input()
    if(arr=='b' or arr=='B'):
        print("BattleShip")
    elif(arr=='c' or arr=='C'):
        print("Cruiser")
    elif(arr=='d' or arr=='D'):
        print("Destroyer")
    elif(arr=='f' or arr=='F'):
        print("Frigate")
