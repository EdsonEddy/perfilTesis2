x = int(input())
for k in range(1,x+1):
    a, b, c = map(int,input().split())
    may = max(a, b, c)
    men = min(a, b, c)
    med = a + b + c - may - men
    print('Case '+str(k)+': '+str(med))