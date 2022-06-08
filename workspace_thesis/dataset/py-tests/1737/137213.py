while True:
    n=int(input())
    if n==0:
        print("error")
    else:
        for i in range(1,n+1,1):
            if i==n:
                print("1"*i)
            else:
                print("1" * i, end=" ")