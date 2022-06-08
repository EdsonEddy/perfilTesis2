s=int(input())
f=1
while (f<=s):
    a=int(input())
    i=0
    c=1
    d=-1
    e=0
    while (i <= a):
        e=d+c
        d=c
        c=e
        i=i+1
    print (e)
    f=f+1