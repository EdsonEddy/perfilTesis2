c = input()
f = input()
cont = 0
for i in range(len(f)):
    if c == f[i]:
        cont += 1
print(cont)