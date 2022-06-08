while True:
    casos=int(input())
    c=0
    for i in range(casos):
        n=input()
        m=""
        for i in n:
            m=i+m
        if m==n:
            c=c+1
    print(c)