from statistics import mode
array=int(input())
variable=input().split()
min=mode(variable)
contador=0
for i in range(array):
    if min!=variable[i]:
        contador+=1
print(contador)