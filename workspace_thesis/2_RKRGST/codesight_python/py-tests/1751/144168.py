cadena=str(input())
sc=0
for i in range(0,len(cadena)):
    l=cadena[i]
    if l=="c":
        sc=sc+1

print(sc)