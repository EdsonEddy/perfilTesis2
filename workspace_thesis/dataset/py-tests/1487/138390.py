def esprimo(x):
    c=True
    for i in range(2,int(x/2)+1):
        if x%i==0:
            c=False
            break;
    return c and x!=1 and x!=0
while True:
    n=int(input())
    if esprimo(n)==True:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
