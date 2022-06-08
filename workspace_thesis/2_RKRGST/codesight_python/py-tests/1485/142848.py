def es(b):
    es=b[::-1]
    if es == b:
        es='si'
    else:
        es='no'
    return(es)


n=int(input())
while n>0:
    c = 0
    for i in range(n):
        pa=input()
        s=es(pa)
        if s == "si":
            c=c+1
    print(c)
    n=int(input())