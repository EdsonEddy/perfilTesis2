v = 0
while(v != ""):
    v=int(input())
    d=int(bin(v)[2:])
    d=str(int(d))
    cadeninv = d[::-1]
    n=int(str(cadeninv))
    print(int(str(n),2))

