def contarC(cad):
    c=0
    for i in range (n):
        if cad[i]== "c":
            c=c+1
    return c

cad = input()
n=len(cad)
c=contarC(cad)
print (c)