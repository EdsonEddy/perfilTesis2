frase = input()
frase = frase.replace(" ","")
long = len(frase)
c = 0
for i in range(long):
    if frase [i] == frase[0]:
        c = c + 1
print(c)