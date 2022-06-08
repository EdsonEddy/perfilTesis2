n,a,b = map(str, input().split(" "))
a,b = int(a), int(b)
x = list(n)
x[a-1], x[b-1] = x[b-1], x[a-1]
for i in x:
    print(i, end = "")