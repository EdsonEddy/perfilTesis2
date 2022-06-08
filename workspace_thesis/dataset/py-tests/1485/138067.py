from sys import stdin
def pal(x):
    y = int(x)
    num = 0
    while x>0:
        d = x%10
        num = int(num*10+ d)
        x = int(x/10)
    if num==y:
        s = True
    else:
        s = False
    return s

for n in stdin:
    n = int(n)
    cuenta = 0
    for i in range(n):
        x = int(input())
        if pal(x):
            cuenta = cuenta + 1
    print(cuenta)