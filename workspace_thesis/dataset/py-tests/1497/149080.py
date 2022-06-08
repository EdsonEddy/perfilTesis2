x1=input()
y1=""
for i in range(len(x1)):
    X=str(bin(ord(x1[i])))
    X=X[2:]
    X=X.zfill(8)
    y1=y1+X
print(y1)