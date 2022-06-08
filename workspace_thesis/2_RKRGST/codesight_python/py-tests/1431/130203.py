n, m, a, b = map(int, input().split())
c = 2
while(n > c):
       f = a + b
       a = b
       b = f
       c = c + 1
x = f % m
print(x)
