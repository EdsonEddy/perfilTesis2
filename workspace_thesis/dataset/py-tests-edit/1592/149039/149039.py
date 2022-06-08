while True:
    n=int(input())
    k=input().split()
    cn=max(set(k), key=k.count)
    r=k.count(cn)
    print(n-r)