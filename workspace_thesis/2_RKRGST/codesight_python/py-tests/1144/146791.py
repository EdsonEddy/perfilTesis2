def primo(n):
    i=2
    while(i*i<=n):
        if(n%i==0):
            return 0
        i=i+1
    return 1

n=int(input())
for i in range (n):
    x=int(input())
    der=x+1
    izq=x-1
    while (primo(der)==0):
        der=der+1
    while (primo(izq)==0):
        izq=izq-1

    print (der + izq)