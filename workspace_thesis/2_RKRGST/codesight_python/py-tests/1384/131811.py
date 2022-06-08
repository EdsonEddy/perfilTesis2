from sys import stdin, stdout
for x in stdin:
    a,b,c = map(int, x.split(" "))
    n = a+b
    res = 0
    while(n >= c):
        res+= n // c
        sobra = n % c
        n = n // c
        n+=sobra
    print(res)
