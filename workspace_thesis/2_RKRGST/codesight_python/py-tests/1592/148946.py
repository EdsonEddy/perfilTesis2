from statistics import mode
array=int(input())
vari=input().split()
min=mode(vari)
cont=0
for k in range(array):
    if min!=vari[k]:
        cont+=1
print(cont)