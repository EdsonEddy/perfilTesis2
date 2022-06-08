import math
n=int(input(""))
for k in range(n):
    t=input("")
    c=0
    x=0
    for i in range(1):
        cad=input("")
        for j in range(len(cad)-1):
            c=int((t.find(cad[j])))-int((t.find(cad[j+1])))
            x=x+abs(c)
        print(x)