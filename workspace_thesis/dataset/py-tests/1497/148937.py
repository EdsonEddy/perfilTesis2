a=input()
b=""
for c in a:
    d=ord(c)
    e=bin(d)
    f,g=e.split("b")
    g="0"+g
    if len(g)!=8:
        while len(g)<8:
            g="0"+g
    b=b+str(g)
print(b)