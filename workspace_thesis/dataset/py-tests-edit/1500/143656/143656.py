n = int(input())
c = input()
v = list(map(int, c.split()))
l = len(v)
for i in range (l -1, -1,-1):
    a = v[i]
for i in range (l):
    b = v [i]
if a == b:
    print("SI")
else:
    print("NO")
