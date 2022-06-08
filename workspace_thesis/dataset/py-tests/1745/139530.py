b = []
x = 1
while x != 0:
    x = (float(input()))
    if x == 0:
        break
    else:
        b.append(x)
c = 0
cn = 0
for i in b:
    c += 1
    if i < 0:
        cn += 1
per = (cn*100)/c
high = max(b)
print(int(per))
print(int(high))