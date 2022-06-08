n = int(input())
for i in range(n):
    x = int(input())
    m = x
    s = 0
    while x>0:
        d = int(x%10)
        x = int(x/10)
        r=1
        for i in range(1,d+1,1):
           r = r*i
        s = int(s+r)
    if s==m:
        print('Y')
    else:
        print('N')

