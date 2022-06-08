cad,r=map(str,input().split())
for i in range(int(r)):
    cad=cad[len(cad)-1]+cad[:(len(cad)-1)]
print(cad)