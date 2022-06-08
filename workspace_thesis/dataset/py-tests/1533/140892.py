while True:
    try:
        n,k = input().split()
    except EOFError:
        break    
    n = int(n)
    k = int(k)
    if n%2==1:
        n+=1
    div = n//2
    if k <= div:
        i = 2*k-1
    else:
        k = k-div
        i = 2*k
    print(i)