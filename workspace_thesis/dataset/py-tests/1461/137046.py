f=int(input())
for g in range (1,f+1):
    a=input()
    d=int(a)**2
    c=0
    e=0
    while 1>0:
        c=0
        for b in a:
            b=int(b)
            c=c+(b**2)
            e=e+1
            a=str(c)
        if c==d and e>=2 or c==4:
            print("Triste")
            break
        elif c==1:
            print('Feliz')
            break