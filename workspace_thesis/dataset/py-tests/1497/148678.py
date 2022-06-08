s=str(input())
for i in s:
    g=str((bin(ord(i))))
    f=g[:1]+g[2:]
    while len(f)<8:
        f='0'+f
    print(f,end="")
print()
