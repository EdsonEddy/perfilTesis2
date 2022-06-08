def vocal(n):
    p=""
    for i in n:
        if i=="A" or i=="a" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U" or i=="y" or i=="Y":
            p=p
        else:
            p=p+i
    return p
n=input()
def minusculas(m):
    pp=""
    for i in vocal(n):
        if i == i.upper():
            pp=pp+i.lower()
        else:
            pp=pp+i
    return pp
m=vocal(n)
def puntos(nn):
    g=""
    for i in minusculas(m):
        f="."+i
        g=g+f
    return g
nn=minusculas(m)
print(puntos(nn))