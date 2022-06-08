while 2>0:
    n=input()
    if n=="":
        break
    c=0
    c1=1
    s=0
    s1=0
    for o in range(len(n)):
        if c >= len(n):
            break
        p=n[c]
        c = c + 2
        s=s+int(p)
    for o in range(len(n)):
        if c1 >= len(n):
             break
        p1 = n[c1]
        c1 = c1 + 2
        s1=s1+int(p1)
    if s==s1:
        print("SI")
    else:
        print("NO")