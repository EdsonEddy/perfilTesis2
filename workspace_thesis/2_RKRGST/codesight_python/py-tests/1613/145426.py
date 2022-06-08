visitas = int(input())
a = set()
for i in range(visitas):
    x = tuple(map(int, input().rstrip().split()))
    a.add(x)
print(len(a))