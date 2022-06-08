a,b = map(str, input().split())
b = int(b)
i=1
while (i <= b):
    a =(a[-1] + a[:-1])
    i = i + 1
print (a)