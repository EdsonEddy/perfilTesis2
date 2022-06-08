cadena=input()
final=[]
for i in cadena:
    def binarizar(n):
        x=bin(n).split("b")
        resp=x[1]
        for j in range(len(resp),8):
            resp="0"+resp
        return resp
    n = ord(i)
    final.append(binarizar(n))
resultado="".join(final)
print(resultado)