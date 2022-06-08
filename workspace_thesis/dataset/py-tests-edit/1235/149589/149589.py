deli = int(input())
choco = list(map(int,input().split()))
c,p1,p2 = 0,0,0
for i in reversed(sorted(choco)):
    c += 1
    if c % 2 == 1:
        p1 += i
    else:
        p2 += i
print(p1-p2)