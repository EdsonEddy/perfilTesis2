n, x = map(int, input().split())
while n!="" \
         "":
    a = input().split()
    s = 0
    for i in range(n):
       s += int(a[(n-i) - 1]) * (x ** i)
    print(float(s))
    n, x = map(int, input().split())
