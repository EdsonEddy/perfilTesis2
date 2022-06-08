x=input()
cad=""
i=0
while i <(len(x)):
    y=str(bin(ord(x[i])))
    y=y[2:]
    y=y.zfill(8)
    cad=cad+y
    i+=1
print(cad)
