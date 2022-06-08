def resto(a):
    for i in range(a):
        r=n[:-a]
    return r
n,b=input().split(" ")
a=int(b)
if a==0:
    print(n)
else:
    def vuelta(m):
        ac = ""
        c = 1
        for i in range(m):
            v = n[-c]
            ac = str(v) + ac
            c = c + 1
        return ac


    m = int(b)
    rr = vuelta(m) + resto(a)
    print(rr)