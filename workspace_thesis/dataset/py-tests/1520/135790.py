def farey(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print('{}/{}'.format(i, j))


# Principal

n = int(input())
farey(n)