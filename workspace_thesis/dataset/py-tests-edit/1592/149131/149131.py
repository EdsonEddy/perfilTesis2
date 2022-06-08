from statistics import mode
arrEEEEy=int(input())
variableSa=input().split()
min=mode(variableSa)
contadorErE=0
for i in range(arrEEEEy):
    if min!=variableSa[i]:
        contadorErE+=1
print(contadorErE)