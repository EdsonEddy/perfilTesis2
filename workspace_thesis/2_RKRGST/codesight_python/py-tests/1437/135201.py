n=int(input())
while(n>0):
    d=n%10
    n=n//10
    if(d==0):
        c=0
        break
    if(d%7==0 or d%4==0):
        c=1
    else:
        c=0
        break
if(c==1):
    print("S")
else:
    print("N")