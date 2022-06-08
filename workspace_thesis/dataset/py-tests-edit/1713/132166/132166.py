from sys import stdin
for n in stdin:
    n = int(n)
    a = 0
    for i in range(1, n+1):
       x = int(input())
       a = a + x
    print(a)