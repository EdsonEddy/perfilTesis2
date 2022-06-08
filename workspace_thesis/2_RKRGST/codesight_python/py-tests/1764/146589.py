def abun(n):
    s=0
    i=1
    while i<n:
        if n%i==0:
            s=s+i
        i=i+1

    if s>n:
       return True

def feliz(n):
    c=0
    j=0
    sw=False
    while n>10 or n==10:
        c=0
        while n>0:
            d=n%10
            n=n//10
            c=c+(d**2)
        n=c
    if  c==1:
        return True


    

a=int(-1e9)
c=int(1e9)
sa=0
sf=0
while True:
    n=int(input())
    if n==-1:
        break
    if n>a:
        a=n
    if n<c:
        c=n
    if abun(n)==True:
        sa=sa+n
    if feliz(n)==True:
        sf=sf+n
print(a)
print(c)
print(sa)
print(sf)