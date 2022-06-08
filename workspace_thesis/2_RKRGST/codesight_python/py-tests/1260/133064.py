n=int(input())
for i in range(n):
    def mcd(a, b):
        resto = 0
        while (b > 0):
            resto = b
            b = a % b
            a = resto
        return a
    a,b = map(int,input().split())
    print(mcd(a, b))