n = int(input())
c = list(map(int, input().split()))
min = abs(c[0]-sum(c[1::]))
for i in range(n):
    if abs(sum(c[:i:]) - sum(c[i::])) < min:
        min = abs(sum(c[:i:]) - sum(c[i::]))
print(min)