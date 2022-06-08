n,m,a,b = map(int, input().split(" "))
x = a
y = b
if(n == 1):
    print(a)
if(n == 2):
    print(b)
for i in range(2, n, 1):
    z = a + b;
    a = b
    b = z
print(z % m)