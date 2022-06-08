n = int(input())
t = []
for x in range(n):
    a, m = map(int, input().split())
    t.append(a % m)
for i in range(len(t)):
    print(t[i])