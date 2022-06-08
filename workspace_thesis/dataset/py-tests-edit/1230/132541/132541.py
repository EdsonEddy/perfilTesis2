n = int(input())
h = n // 3600
n = n % 3600
m = n // 60
s = n % 60
if m > 60:
    rm = m % 60
    h = h + 1
    m = m - rm
elif m == 60:
    h = h + 1
    m = m - 1
if s > 60:
    rs = s % 60
    s = s - rs
    m = m + 1
elif s == 60:
    m = m + 1
    s = s - 1
print(h,m,s)