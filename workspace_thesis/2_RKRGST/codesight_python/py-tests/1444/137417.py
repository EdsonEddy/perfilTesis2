n=int(input())
y=0
p=0
i=1
k=0
while i<=n:
    v = int(input())
    b = 0
    c = 0
    while v != 0:
        b = str(b) + str(v % 2)
        v = int(v / 2)
    h = int(b)
    while h > 0:
        x = h % 10
        h = h // 10
        if x == 1:
            y = y + 1
        else:
            y=0
        if y == 2:
            p=p+1
            y=0
    y=0
    print(p)
    i=i+1
    p=0