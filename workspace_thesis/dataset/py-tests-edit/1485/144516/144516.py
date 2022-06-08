while True:
    n=int(input())
    c=0
    for i in range(n):
        r=str(input())
        s=r[::-1]
        if r==s:
            c+=1
    print(c)