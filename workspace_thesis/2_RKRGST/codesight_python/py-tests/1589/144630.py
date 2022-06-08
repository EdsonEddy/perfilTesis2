entrada = input()
entrada = entrada.lower()
ls = []
for i in entrada:
    ls.append(ord(i))
ls.sort()
c = 97
while c in ls:
    c += 1
if c > 122:
    print(-1)
else:
    print(chr(c))