while True:
    a=list(input().upper())
    A=set(a)
    A=list(A)
    A.sort()
    for i in range(len(A)):
        c=a.count(A[i])
        print(str(A[i])+'='+str(c))
    print()