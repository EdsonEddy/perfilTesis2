modificar=input()
X=""
for i in range(len(modificar)):
    mensaje=str(bin(ord(modificar[i])))
    mensaje=mensaje[2:]
    mensaje=mensaje.zfill(8)
    X=X+mensaje
print(X)