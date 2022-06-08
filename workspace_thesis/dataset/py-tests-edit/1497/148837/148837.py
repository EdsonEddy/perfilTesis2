def ascii_to_bin(i):
    la = ord(i)
    cod = []
    while (la > 0):
        if (la & 1) == 1:
            cod.append("1")
        else:
            cod.append("0")
        la = la >> 1
    cod.reverse()
    b = "".join(cod)
    z = (8 - len(b)) * '0'
    return z + b
c = str(input())
b = []
for i in c:
    b.append(ascii_to_bin(i))
print("".join(b), end="")