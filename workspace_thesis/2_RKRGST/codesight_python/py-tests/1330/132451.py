cad, R = input().split()
R = int(R)
s = ''
for i in range(-1, -R - 1, -1):
    s = cad[i] + s
print(s + cad[:len(cad) - R])