while True:
    a=input()
    l=[]
    lac=[]
    for i in range(len(a)):
        l.append(a[i])
    l.sort()
    for j in range(len(l)):
        b=0
        x=j
        if l[x] not in lac:
            b=l.count(l[x])
            lac.append(l[x])
            print(l[x],end="")
            print("=",end="")
            print(b)
    print("")