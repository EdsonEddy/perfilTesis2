prueva=int(input())
while prueva>0:
    numero=int(input())
    X=1
    numero=numero%6
    for i in range(numero+1):
        X=X*2
        if X>=10:
            X=X%10+X//10
    print(X)
    prueva-=1