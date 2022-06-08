import sys 
def capicuo(x):
    Y = 0
    while (x>0):
        n = x%10
        Y = Y*10 + n
        x = int(x/10)
    return(Y)
for x in sys.stdin:
    n =int(x)
    c = 0
    for i in range(1, n+1):
        x = int(input())
        a = x
        if capicuo(x) == a:
            c = c+1
    print(c)