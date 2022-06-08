while True:
    try:
        x=int(input())
        l=[int(x) for x in input().split()]
        if len(l)==x:
            y=int(l[-1])
            c=0
            for i in range(x):
               if l[i]==y:
                   c+=1
            print(c)
    except ValueError:
        break