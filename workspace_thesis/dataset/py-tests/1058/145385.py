x = int(input())
for i in range(x):
    lon = int(input())
    elements = input().split()
    for j in range(len(elements)):
        elements[j] = int(elements[j])
    aux = sorted(elements)
    print(*aux)