n=int(input())
for i in range(n):
    p = int(input())
    a, b = map(int, input().split())
    s = str(a) + "+" + str(b)
    if p==1:
        print(a)
        continue
    if p==2:
        print(s)
        continue

    for i in range(p-2):
        c=a+b
        a,b=b,c
        s=s+"+"+str(c)
    print(s)