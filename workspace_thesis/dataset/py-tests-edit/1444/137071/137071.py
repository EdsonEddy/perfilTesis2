n=int(input())
l=[]
for i in range(n):
    c=int(input())
    if n<=255:
        if c<2**25:
            c=bin(c)
            l.append(c)
            l=str(l)
            print(l.count("11"))
            l=[]
            c=0