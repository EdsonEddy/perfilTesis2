n = int(input())
v = list(map(int, input().split()))
c = [0]*101
for i in range(n):
    c[v[i]] += 1
print(n-max(c))