def fac(n):
    i,m = 1,1
    for i in range(1,n+1):
        m = m*i
    return m

n = int(input())
for i in range(n):
    x = int(input())
    y = x
    s = 0
    while x>0:
        d = (x%10)
        s = int(s+fac(d))
        x = int(x/10)
    if s==y:
        print('Y')
    else:
        print('N')

