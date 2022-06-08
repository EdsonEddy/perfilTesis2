from statistics import mode
igualar=int(input())
C =input().split()
x=mode(C)
array=0
for i in range(igualar):
    if x!=C[i]:
        array+=1
print(array)