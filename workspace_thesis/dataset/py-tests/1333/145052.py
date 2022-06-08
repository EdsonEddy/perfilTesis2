a = input()
n = [] * len(a)
for i in range(len(a)):
    n.append(a[i:])
n.sort()
for i in range(len(n)):
    print(n[i])
