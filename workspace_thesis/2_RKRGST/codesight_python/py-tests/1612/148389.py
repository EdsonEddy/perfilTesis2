while 1>0:
    n=str(input())
    l=list(n)
    j=[]
    for i in l:
        if i not in j:
            j.append(i)
    j=sorted(j)
    for h in j:
        f=l.count(h)
        print(h,end="")
        print("=",end="")
        print(f)
 
    print()