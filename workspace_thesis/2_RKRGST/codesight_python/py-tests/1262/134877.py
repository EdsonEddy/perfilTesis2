def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)
n = int(input())
while(n!=0):
    s = input()
    v = s.split()
    a = int(v[0])
    b = int(v[1])
    print(mcd(a, b))
    n = n - 1