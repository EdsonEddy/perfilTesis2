cad = input()
c = 0
for i in range(len(cad)):
    a = cad[i]
    a = a.upper()
    
    if (a == "C"):
        c = c + 1
print(c)
