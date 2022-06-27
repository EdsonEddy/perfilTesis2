import sys
n=int(sys.stdin.readline())
for i in range(n):
    n,k= map(int,sys.stdin.readline().split())
    aux=''
    sum2=0
    numb=0
    for letra in str(n):
        numb=numb+1
    while n>0:
        m=n//10
        sum,sum2=0,0
        for j in range(k):
            x = n % 10
            n=n//10
            sum = sum + x

        while sum!=0 or sum2>=10:
            auxsum=sum%10
            sum=sum//10
            sum2=sum2+auxsum
            if sum==0 and sum2>=10:
                sum=sum2
                sum2=0

        aux =str(sum2)+ aux
        if n!=0:
            n=m
    if (k>numb):
        aux=''
    print(aux)
