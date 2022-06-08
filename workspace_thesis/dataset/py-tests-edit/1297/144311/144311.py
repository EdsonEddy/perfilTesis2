num=int(input())
for i in range(num):
    cad=str(input())
    cad1= ''
    for j in range(len(cad)+1):
        a=cad[len(cad)-j:len(cad)-j+1]
        cad1 = cad1 + a
    print(cad1)