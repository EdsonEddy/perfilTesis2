x = int(input())
h = x//3600
x %= 3600
m = x//60
print(h, m, x%60)