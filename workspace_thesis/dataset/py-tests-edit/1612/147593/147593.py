while True:
    l=input()
    r=list(l)
    r=list(set(r))
    con=[]
    s=""
    r.sort()
    c=0
    for i in range(len(r)):
        for j in range(len(l)):
            if r[i]==l[j]:
                c+=1
        s=str(r[i])+"="+str(c)
        con.append(s)
        c=0
    for k in range(len(con)):
        print(con[k])
    print()
