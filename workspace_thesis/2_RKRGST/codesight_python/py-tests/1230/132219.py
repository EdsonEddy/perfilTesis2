from sys import stdin
for n in stdin:
    n = int(n)
    x = n
    h = int(x/3600)
    x = int(x-h*3600)
    m = int(x/60)
    s = int(x-m*60)
    print("{:d} {:d} {:d}".format(h,m,s))