
def digitos(n):
    sumdigit=0
    while n!=0:
        ext=n%10
        n//=10
        sumdigit+=ext
    return sumdigit 
v=[0]*10010
for i in range(1,10010-1):
    v[i]=digitos(i)
while True:
    n,a,b=map(int,input().split())
    s=0
    for i in range(1,n+1):
        if v[i]>=a and v[i] <=b:
            s+=i
    print(s)