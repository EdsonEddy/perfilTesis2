n=int(input())
num=1
d=1
k="/"
q=n
p=n
while(n!=0):
    while(p!=0):
        z=str(num) + str(k) + str(d)
        print(z)
        d=d+1
        p=p-1
    n=n-1
    d=1
    num=num+1
    p=q