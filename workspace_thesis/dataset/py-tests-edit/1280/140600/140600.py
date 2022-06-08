def leevector (p,A,n,s):
    v=s.split(" ")
    for k in range (n-1):
        x= int(v[k])
        A.append(x)
    i=0
    for j in range (1,n+1,1):
        A= sorted(A)
        if A[n-2]!= n:
                p=n
        while i<=n-2:
            if(A[i])==j:
                i=i+1
                break
            else:
                p=j
                i=i
                break
    return p
while True:
    n=int(input())
    s=input()
    A=[]
    p=0
    print(leevector (p,A,n,s))
