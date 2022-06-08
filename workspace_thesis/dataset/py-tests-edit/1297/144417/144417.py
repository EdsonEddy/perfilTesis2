n=int(input())
for i in range (n):
    cad=input()
    ta=len(cad)
    nc=''
    for j in range (ta):
        ta = ta - 1
        l=cad[ta]
        nc=nc+l
    print(nc)
