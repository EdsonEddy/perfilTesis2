while True:
    n=input()
    x=[]
    for i in n:
        if i not in x:
            x.append(i)
    x.sort()
    result=[]
    for i in x:
        f=n.count(i)
        result.append(f)
    for i in range(len(x)):
        p=str(result[i])
        print(x[i]+"="+p)
    print()