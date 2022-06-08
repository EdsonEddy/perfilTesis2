from statistics import mode

cant=int(input())
elementos=input().split()
dife=mode(elementos)
cont=0

for i in range(cant):
    if dife!=elementos[i]:
        cont+=1
print(cont)
