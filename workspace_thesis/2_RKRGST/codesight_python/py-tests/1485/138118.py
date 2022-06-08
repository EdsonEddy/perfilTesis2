def invierte (n):
    m = 0
    while n>0:
        d = n%10
        m = m*10+d
        n= n//10
    return (m)

a=int(input())
c=0
for i in range (1,a+1):
    n= int(input())
    if n==invierte(n):
        c=c+1
print(c)
k=int(input())
c1=0
for i in range (1,k+1):
    n= int(input())
    if n==invierte(n):
        c1=c1+1
print(c1)
