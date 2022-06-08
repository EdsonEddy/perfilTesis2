while True:
    n=int(input())
    def uno():
        c = 1
        cc = 1
        li2 = []
        for i in range(n):
            li2.append(c)
            if c == cc:
                c = c + 1
                cc = 0
            cc = cc + 1
        return li2
    def dos():
        li = []
        c1 = 0
        cv = 1
        com = 1
        for i in range(n):
            li.append(c1)
            if cv == com:
                cv = 0
                c1 = -1
                com = com + 1
            c1 = c1 + 1
            cv = cv + 1
        return li
    s=""
    p=1
    for i in range(n):
        p1=2**uno()[i]
        p2=2**dos()[i]
        r=p1+p2
        if p==1:
            s=s+str(r)
        else:
            s=s+" "+str(r)
        p=p+1
    print(s)