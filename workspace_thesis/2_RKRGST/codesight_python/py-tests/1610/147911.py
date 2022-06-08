while True:
    n=input()
    l=[]
    R=[]
    for i in range(int(len(n))):
        if n[i]=="0" :
            r=l.count("1")
            R.append(r)
            l=[]
            continue
        else:
            r=n[i]
            l.append(r)
    if True:
        r=l.count("1")
        R.append(r)
        for i in range(len(R)):
            if i<(len(n)-1):
                print(R[i], end="")