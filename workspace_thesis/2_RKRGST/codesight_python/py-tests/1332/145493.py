cad=input()
cad=cad.lower()
for i in range(len(cad)):
    h=cad[i]
    if h!="a" and h!="e" and h!="i" and h!="o" and h!="u" and h!="y":
        print(".", end=h)
