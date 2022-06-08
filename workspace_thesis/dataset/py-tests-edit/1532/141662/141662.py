import sys
for n in sys.stdin:
    n=int(n)
    dig=[]
    while n>0:
        dig.append(n%10)
        n//=10
    dig.sort()
    for i in range(len(dig)):
        print(dig[i],end="")
    print("")
