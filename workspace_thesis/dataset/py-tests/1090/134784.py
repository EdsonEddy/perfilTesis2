n=input()
n=int(n)

if n<3:
    print(0)
else :
    x=1
    c=0
    while c<n :
         c=x*3+c
         x=x+1
    print(c)