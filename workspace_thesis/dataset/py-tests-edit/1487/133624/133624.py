while True:
    n=int(input())
    def esprimo(n):
        if n==1: return 0
        if n==2: return 1
        i=3
        while i*i <= n:
            if(n % i==0): return 0
            i+=2
        return n%2

    v=esprimo(n)
    if v == 0:
        print("NO ES PRIMO")
    else:
        print("ES PRIMO")