frase = input()
c = ord('c')
v = [0 for i in range(260)]
for i in range(len(frase)):
    v[ord(frase[i])]+=1
print(v[c])