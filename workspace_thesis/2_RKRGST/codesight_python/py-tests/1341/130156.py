s=''
while True:
    a=input()
    i=0
    c=1
    d=-1
    e=0
    if (str(a) == s):
        break
    else:
        a=int(a)
        while (i <= a):
            e=d+c
            d=c
            c=e
            i=i+1
        print (e)