cad = input()

while cad != "#":
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    g = ""
    for i in range(len(cad)):
        if (cad[i] == chr(37)):
            a = a + "%25"
        else:
            a = a + cad[i]
    for i in range(len(a)):
        if (a[i] == chr(32)):
            b = b + "%20"
        else:
            b = b + a[i]
    for i in range(len(b)):
        if (b[i] == chr(33)):
            c = c + "%21"
        else:
            c = c + b[i]
    for i in range(len(c)):
        if (c[i] == chr(36)):
            d = d + "%24"
        else:
            d = d + c[i]
    for i in range(len(d)):
        if (d[i] == chr(40)):
            e = e + "%28"
        else:
            e = e + d[i]
    for i in range(len(e)):
        if (e[i] == chr(41)):
            f = f + "%29"
        else:
            f = f + e[i]
    for i in range(len(f)):
        if (f[i] == chr(42)):
            g = g + "%2a"
        else:
            g = g + f[i]
    
    
    print(g)
    cad = input()
    
