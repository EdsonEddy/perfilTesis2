tex=input()
s=""
for i in tex:
    a=bin(ord(i))
    if len(a[2:])<8:
        dif=8-len(a[2:])
        s=s+"0"*dif+a[2:]
    else:
        s=s+a[2:]
print(s)