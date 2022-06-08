n = int(input())
for x in range(n):
    c = input().split()
    break
e = n
m = n
sw = 1
while(sw == 1 and e <= m):
    i = c[e - n]
    f = c[m - 1]
    e = e + 1
    m = m - 1
    if(int(i) != int(f)):
        sw = 0

if(sw == 1):
    print("SI")
else:
    print("NO")