l = input().split()
cad = l[0]
n = int(l[1])
cad = cad + cad
a = len(cad)//2 - n
b = len(cad) - n
print(cad[a:b])