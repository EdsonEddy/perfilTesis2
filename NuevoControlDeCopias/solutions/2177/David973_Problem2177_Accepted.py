casos=int(input())
for i in range (casos):
    n,k=map(int,input().split(" "))
    kk=n%(10)**k
    n=n//10
    nuevo=0
    pot=0
    while(n>0):
        s=0
        tamkk=int(len(str(kk)))
        while(kk>0 and tamkk==k):
            dig=kk%10
            kk=kk//10
            s=s+dig
        while (s>9):
            s=(s%10)+(s//10)
        nuevo=nuevo+(s*10**pot)
        pot=pot+1
        kk=n%(10)**k
        n=n//10
    if (nuevo !=0):
        print(nuevo)
