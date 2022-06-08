from statistics import mode
veces=int(input())
item =input().split()
gok=mode(item)
gojan=0
for i in range(veces):
    if gok!=item[i]:
        gojan+=1
print(gojan)