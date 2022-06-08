s = int(input())
for y in range(s):
    n = int(input())
    m = input().split()
    if n==len(m):
        d = 0
        for x in m:
            c = int(x)
            if c%3==0:
                d += c*2
        print("La suma es",d)