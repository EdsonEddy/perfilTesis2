import math
r = int(input())
for i in range (r):
    n = int(input())
    x = n
    nc = n
    s = 0
    while n > 0:
          x = n % 10
          n = n // 10
          fact = math.factorial(x)
          s = s + fact
    if s == nc:
       print("Y")
    else:
       print("N")