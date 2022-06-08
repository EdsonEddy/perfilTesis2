x = int(input())
for i in range(x):
    a = int(input())
    r = 10**(a-1)
    lo = str(r)
    lo = len(lo)
    res = 2**(lo-1)
    print(res)