def mcd(a, b):
    r = 0
    while(b > 0):
        r = b
        b = a % b
        a = r
    return a
casos=int(input())
for k in range(casos):
    num1, num2 = map(int, input().split())
    m=mcd(num1, num2)
    print(m)