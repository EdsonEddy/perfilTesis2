def esPalindromo(x):
    return x==int(str(x)[::-1])
while True:
    n=int(input())
    s=0
    for i in range(1,n+1):
        x=int(input())
        if esPalindromo(x) == True:
            s=s+1
    print(s)
