m,x=map(int,input().split())
while m!=""\
    "":
    a=input().split()
    s=0
    for i in range(m):
        s+=int(a[(m-i)-1])*(x**i)
    print(float(s))
    m,x=map(int,input().split())