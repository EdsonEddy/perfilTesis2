s=input()
c=""
for i in s:
    x=bin(ord(i))
    g=len(x)-2
    if g==8:
        c=c+x[2:]
    else:
        k=8-g
        c=c+"0"*k+x[2:]
print(c)