l, r, k = map (int, input().split(" "))
cot = 0
for i in range (l, r+1):
    if i % k == 0:
        cot = cot + 1
print (cot)
