import sys
for n in sys.stdin:
    n=int(n)
    v=[]
    while (n>0):
        v.append(n%10)
        n//=10
    v.sort()
    for i in range (len(v)):
        print(v[i],end="")
    print("")
