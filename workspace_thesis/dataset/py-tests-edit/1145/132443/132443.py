casos=int(input())
for i in range(casos):
    a,b=0,1
    n=int(input())
    for y in range(n):
        a,b=b,a+b
    print(a) 