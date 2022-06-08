o=0
while o!="":
    k,t=map(int,input().split())
    n=0
    pt=0
    while pt!=t:
        for i in range(0,18,1):
            a=(2**n)*k
            pt=pt+a
            n=n+1
            if pt==t:
                print(n)
                break