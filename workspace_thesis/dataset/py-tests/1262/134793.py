nc = int(input())
for i in range(nc):
    a,b = map(int,input().split())
    may = max(a, b)
    men = min(a, b)
    c = may // men
    r = may % men
    # print(r)
    while r != 0:
        may = men
        men = r
        c = may // men
        r = may % men
    print(men)