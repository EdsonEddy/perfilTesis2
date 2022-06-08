a,b = map(int,input().split())
c=0
if a==1:
    a=a+1
for n in range(a,b+1):
    # Proceso
    i = 2
    esPrimo = True
    while i*i<=n:
        if n % i == 0:
             esPrimo = False
             break
        i = i +1
    if esPrimo:
            c=c+1
print(c)
    