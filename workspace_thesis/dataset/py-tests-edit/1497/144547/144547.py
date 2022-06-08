n=str(input())
s=""
for i in n:
    f=(bin(ord(i))[:1]+bin(ord(i))[2:])

    while len(f)<8:
        f='0'+f
    print(f,end="")
print()