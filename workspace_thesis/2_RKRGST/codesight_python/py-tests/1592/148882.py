n = int(input())
m = list(map(int, input().split()))
m.sort()
x = 0
cp = 0
cti = 1
mx = -1
while x < len(m) - 1:
    if m[x] == m[x + 1]:
        x = x + 1
        cti = cti + 1
    else:
        if cti >= mx:
            mx = cti
        cti = 1
        x = x + 1
if mx >= cti:
    print(len(m) - mx)
else:
    print(len(m) - cti)
