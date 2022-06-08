z=int(input())
for i in range(z):
    n=input()
    r=0
    x=0
    while x!=1:
        for i in n:
            r = r + (int(i) ** 2)
        n=str(r)
        if len(n) == 1:
            x=1
        else:
            r=0
    if n=="1":
        print("Feliz")
    else: print("Triste")
