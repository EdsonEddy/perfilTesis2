z=int(input())
for i in range(z):
    n=str(input())
    s=len(n)
    r=0
    x=0
    while x!=1:
        for i in range(s):
            d=int(n[i])
            r=r+d**2
        n=str(r)
        s=len(n)
        if s==1:
            x=1
        else:
            r=0
    if n=="1":
        print("Feliz")
    else:
        print("Triste")