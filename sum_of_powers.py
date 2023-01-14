number=list(map(int,input().split()))
total=0
for i in range(len(number)):
    x=str(number[i])
    length=len(x)
    if length==2:
        power=int(x[0])**int(x[1])
        total+=power
    elif length==1:
        power=0
        total+=power
    elif length>2:
        power=int(x[:length-1])**int(x[length-1])
        total+=power
print(total)       