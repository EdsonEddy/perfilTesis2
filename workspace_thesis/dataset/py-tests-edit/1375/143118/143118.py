cadena=str(input())
cadena= cadena.lower()
x=len(cadena)
sw=0
for i in range (0,x+1):
    sw=0
    if i<x-2:
        if cadena[i] == "o":
            if cadena[i+1] == "r":
                if cadena[i+2] == "o":
                    print(i,end=" ")
                    print(i + 2)
                    sw=1
                    break
if sw==0:
    print("-1")
        