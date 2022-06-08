while True:
    a,s = [],0
    a = input().split()
    for i in a:
        i = int(i)
        if i!=0:
            s = s+i
    print(s)