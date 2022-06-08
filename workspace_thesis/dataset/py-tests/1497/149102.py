H=input()
O=""
for i in range(len(H)):
    X=str(bin(ord(H[i])))
    X=X[2:]
    X=X.zfill(8)
    O=O+X
print(O)