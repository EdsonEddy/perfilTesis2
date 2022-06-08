n=input()
x=""
for i in range(len(n)):
    by=str(bin(ord(n[i])))
    by=by[2:]
    by=by.zfill(8)
    x=x+by
print(x)