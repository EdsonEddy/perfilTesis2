def par( t ):
    t = int(t)
    p = t*2
    return p

n = int(input())
a = 0
b = 1
f = 1
p = 1
for i in range (1,n+1,1):
    if i % 2 == 1:
        print(f)
        f = a + b
        a = b
        b = f
    else:
        print(par(p))
        p = p + 1
