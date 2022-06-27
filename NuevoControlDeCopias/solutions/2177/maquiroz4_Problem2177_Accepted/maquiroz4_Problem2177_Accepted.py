import math

ncasos=int(input())
for _ in range(ncasos):
    n_original, k= map(int, input().split())
    n=n_original
    c=0
    sum=0
    t=int(math.log10(n))+1
    p=0
    sum_dig=0
    while t>=k:
        c=c+1
        #Desconpone digito de la derecha del numero
        dig=n%(10**k)

        # suma digito
        num = dig
        while num > 9:
            suma = 0
            while num:
                suma, num = suma + num % 10, num // 10
            num = suma

        sum_dig=num*(10**p)+sum_dig
        #print(t, n, dig, num, sum_dig)
        p=p+1

        n=n//(10**2)
        n=int(n_original//(10**c))
        t=t-1
    if sum_dig!=0:
        print(sum_dig)
