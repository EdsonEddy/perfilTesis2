def encuentra(n):
    x=n.find("oro")
    h = n.find("OrO")
    f = n.find("oRo")
    g = n.find("ORO")
    gd = n.find("ORo")
    gg = n.find("oRO")
    ggg = n.find("Oro")
    yy = n.find("orO")
    if x!=-1:
        return x
    elif h!=-1:
        return h
    elif g!=-1:
        return
    elif gd!=-1:
        return gd
    elif gg!=-1:
        return gg
    elif ggg!=-1:
        return ggg
    elif yy!=-1:
        return yy
    elif f!=-1:
        return f
    else:
        return -1
n=input()
otro=encuentra(n)+2
if encuentra(n)!=-1:
    print(encuentra(n), otro)
else:
    print(-1)