while True:
    x=input().split()
    s=0
    for i in range(len(x)):
        s=s+int(x[i])
    print(s)