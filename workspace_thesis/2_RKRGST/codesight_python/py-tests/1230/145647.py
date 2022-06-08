time = int(input())
a = time // 3600
time %= 3600
i = time // 60
time %= 60
print(a, i, time)