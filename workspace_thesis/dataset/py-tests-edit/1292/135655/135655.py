while True:
    a,s = [],0
    m=int(input())
    if m==0:
        break
    a = input().split()
    for i in a:
        i = int(i)
        if i!=0:
            s = s+i
    print(s)