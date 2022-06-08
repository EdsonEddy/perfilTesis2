x = int(input())
for j in range(x):
    n = input()
    for i in range(len(n) - 1, -1, -1):
        print(n[i], end='')
    print()