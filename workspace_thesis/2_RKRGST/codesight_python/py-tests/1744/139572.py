n=int(input())
l=str(n)
g=n
c=1
while n>0:
    s = ""
    s1 = ""
    for i in range(1,n+1,1):
        s=s+str(i)
    s1=s[::-1]
    if n==g-1:
        print(str(s)+str(l)+str(s1))
        l = " " * c
        print(str(s) + str(l) + str(s1))
        c = c + 2
    elif g!=n:
        l = " " * c
        print(str(s) + str(l) + str(s1))
        c=c+2
    n=n-1

