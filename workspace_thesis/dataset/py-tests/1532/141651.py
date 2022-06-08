from sys import stdin
for n in stdin:
    n = int(n)
    f = []
    while n>0:
        d = n%10
        n//= 10
        f.append(d)
    f.sort()
    for i in range(len(f)):
        print(f[i],end="")
    print("")
    