def busqueda(n):
    m = ""
    for i in n:
        if i == "_":
            m = m + " "
        elif i == "-":
            m = m + "-"
        elif i == ",":
            m = m + ","
        elif i == ".":
            m = m + "."
        else:
            s = ord(i)
            f = s + a
            while f > 122:
                f=f-96
                f=f%26
                f=f+96
            g = chr(f)
            m = m + g
    return m
while 2 > 0:
    b, n = input().split(" ")
    b=int(b)
    b=b%26
    a = int(b)
    busqueda(n)
    dd = busqueda(n).upper()
    print(dd)