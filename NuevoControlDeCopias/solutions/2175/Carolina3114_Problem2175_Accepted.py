for _ in range(int(input())):
    x=int(input())
    f = [0]
    m,n=1,0
    for i in range (100):
        if x in f:
            print(len(f)-1)
            break
        y = m + n
        f.append(y)
        m=n
        n=y

