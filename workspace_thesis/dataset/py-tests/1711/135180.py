import  math
casos=int(input())
for x in range(casos):
    n=int(input())
    s=0
    if n!="fin":
        for d in range(n):
            m=int(input())
            s=s+m
        print(s)