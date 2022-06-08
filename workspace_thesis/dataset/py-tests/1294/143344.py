n = int(input())
for a in range(n):
    x = input().split()
    y = input().split()
    s = 0
    for i in range(int(x[0])):
        if i == int(x[1]):
            for j in range(i, int(x[2]) + 1):
                s = s + int(y[j])
    print(s)