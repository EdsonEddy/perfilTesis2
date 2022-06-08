n, i, j = input().split()
n = list(n)
i, j = int(j)-1, int(i)-1
n[i], n[j] = n[j], n[i]
print(''.join(str(x) for x in n))