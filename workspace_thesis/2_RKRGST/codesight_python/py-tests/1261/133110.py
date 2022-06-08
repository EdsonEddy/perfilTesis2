n=int(input())
p=1
for i in range(n):
    a,b = map(int, input().split())
    p=1
    for j in range(b):
        p=p*a
    print(p)