a,b = map(int,input().split())
p=0
if(a==1):
    a=a*2
for n in range(a,b+1):
    i = 2
    esPrimo = True
    while i * i <= n:
        if n % i == 0:
            esPrimo = False
            break
        i = i + 1
    if esPrimo:
        p=p+1
print(p)