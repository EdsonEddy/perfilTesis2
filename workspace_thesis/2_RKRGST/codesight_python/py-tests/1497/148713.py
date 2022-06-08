cad = input()
n = ''
def con8(c):
    while len(c) != 8:
        c = '0' + c
    return c
for i in cad:
    n = n + con8(bin(ord(i))[2::])
print(n)

