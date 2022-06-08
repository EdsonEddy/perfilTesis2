def reem(c,l):
    c = c.lower()
    for i in range(l):
        e = c[i]
        if e != "a"and e !="e" and e !="i"and e !="o"and e !="u" and e !="y":
            print(".", end=e)


c = input()
l = len(c)
reem(c,l)