a, des = map(int,input().split())
bo = list(map(int,input().split()))
c = 0
i = 0
while c < len(bo) and bo[i] != des:
    i = bo[i]
    c += 1
if bo[i] == des:
    print("SI")
else:
    print("NO")