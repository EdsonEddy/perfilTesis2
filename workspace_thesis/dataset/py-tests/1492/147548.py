def encontrar(t,c,l):
    s = 0
    for i in range(l):
        if t[i] == c:
            print(i)


t = input()
c = input()
l = len(t)
encontrar(t,c,l)