k=int(input())
for q in range(k):
    n=int(input())
    c=n//2
    r=''
    if c>=1:
        for i in range(c):
            r=r+str(8)
        if n%2!=0:
            r=r+str(4)
    r=r[::-1]
    if n==1:
        r=r+str(0)
    if n==0:
        r=r+str(1)
    print(r)
